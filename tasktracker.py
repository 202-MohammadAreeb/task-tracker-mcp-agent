from mcp.server.fastmcp import FastMCP
import json
import os
from typing import List, Dict

mcp = FastMCP("TaskTracker")
TASK_FILE = "tasks.json"

def load_tasks() -> List[Dict]:
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks: List[Dict]):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

@mcp.tool()
def add_task(title: str, due_date: str, assigned_to: str) -> str:
    tasks = load_tasks()
    task = {
        "title": title,
        "due_date": due_date,
        "assigned_to": assigned_to,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    return f"Task '{title}' added for {assigned_to}."

@mcp.tool()
def get_tasks(assigned_to: str) -> List[Dict]:
    tasks = load_tasks()
    user_tasks = [t for t in tasks if t["assigned_to"].lower() == assigned_to.lower()]
    return user_tasks

@mcp.tool()
def mark_done(title: str) -> str:
    tasks = load_tasks()
    for task in tasks:
        if task["title"].lower() == title.lower():
            task["done"] = True
            save_tasks(tasks)
            return f"Task '{title}' marked as done."
    return f"Task '{title}' not found."

@mcp.tool()
def delete_task(title: str) -> str:
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t["title"].lower() != title.lower()]
    if len(updated_tasks) < len(tasks):
        save_tasks(updated_tasks)
        return f"Task '{title}' deleted."
    else:
        return f"Task '{title}' not found."
    
@mcp.tool()
def get_all_assignees() -> List[str]:
    tasks = load_tasks()
    assignees = list({t["assigned_to"] for t in tasks})
    return assignees

@mcp.tool()
def count_pending_tasks() -> int:
    tasks = load_tasks()
    pending = [t for t in tasks if not t.get("done", False)]
    return len(pending)

@mcp.tool()
def list_pending_tasks_with_assignees() -> List[Dict[str, str]]:
    """
    Returns a list of pending tasks with their titles and assigned users.
    """
    tasks = load_tasks()
    pending = [
        {"title": t["title"], "assigned_to": t["assigned_to"]}
        for t in tasks if not t.get("done", False)
    ]
    return pending


@mcp.tool()
def who_is_assigned(title: str) -> str:
    tasks = load_tasks()
    for task in tasks:
        if task["title"].lower() == title.lower():
            return f"{task['assigned_to']} is assigned to '{title}'."
    return f"No one is assigned to '{title}'."

@mcp.tool()
def list_tasks_by_status(status: str) -> List[Dict]:
    tasks = load_tasks()
    is_done = status.lower() == "done"
    filtered = [t for t in tasks if t["done"] == is_done]
    return filtered


from datetime import datetime

@mcp.tool()
def get_overdue_tasks() -> List[Dict]:
    tasks = load_tasks()
    now = datetime.now()
    overdue = []
    for task in tasks:
        if not task["done"]:
            try:
                due_date = datetime.strptime(task["due_date"], "%Y-%m-%d")
                if due_date < now:
                    overdue.append(task)
            except ValueError:
                continue
    return overdue

@mcp.tool()
def show_all_tasks() -> List[Dict]:
    """
    Returns all tasks in the system.
    """
    return load_tasks()

if __name__ == "__main__":
    print("TaskTracker MCP tool running...")
    mcp.run(transport="stdio")
