from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")
# Load environment variables
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": None})

@app.post("/", response_class=HTMLResponse)
async def post_prompt(request: Request, prompt: str = Form(...)):
    response = await run_agent(prompt)
    return templates.TemplateResponse("index.html", {"request": request, "response": response})

# Core agent function
async def run_agent(prompt: str):
    client = MultiServerMCPClient({
        "tasktracker": {
            "command": "python",
            "args": ["tasktracker.py"],
            "transport": "stdio",
        }
    })

    tools = await client.get_tools()
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    agent = create_react_agent(model, tools)

    result = await agent.ainvoke({"messages": [{"role": "user", "content": prompt}]})
    return result["messages"][-1].content
