
🧠 TASK TRACKER MCP AGENT

An AI-powered task tracking assistant that lets you manage tasks using natural language — built with LangChain MCP, FastAPI, and Google Gemini.

────────────────────────────────────────────

✨ FEATURES

- ✅ Add new tasks with title, due date, and assignee
- ✅ Get tasks by user, status (done/pending), or overdue
- ✅ Mark tasks as done or delete them by name
- ✅ List assignees and count pending tasks
- ✅ Simple web interface using FastAPI + Jinja2
- ✅ Powered by Gemini 2.0 (via LangChain's Google Generative AI)
- ✅ Local JSON-based storage (no database required)

────────────────────────────────────────────

🚀 GETTING STARTED

1. Clone the repo:
   git clone https://github.com/202-MohammadAreeb/task-tracker-mcp-agent.git
   cd task-tracker-mcp-agent

2. Install dependencies:
   pip install -r requirements.txt

3. Set up your .env file:
   GOOGLE_API_KEY=your_api_key_here

4. Run the app:
   cd task_ui
   uvicorn main:app --reload

────────────────────────────────────────────

💬 EXAMPLE PROMPTS

- "Add task 'Submit report' for Alice due 2025-08-05"
- "What tasks are overdue?"
- "Who is assigned to 'Design Mockups'?"
- "Mark 'Review PR' as done"

────────────────────────────────────────────

🛠️ BUILT WITH

- LangChain MCP + LangGraph
- FastAPI + Jinja2
- Google Gemini (via langchain-google-genai)
- Python 3.11

────────────────────────────────────────────

📬 CONTACT

- areeb.syed2225@gmail.com
- https://www.linkedin.com/in/mohammad-areeb-8050a6222/
