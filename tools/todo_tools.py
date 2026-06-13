# tools/todo_tools.py
import json
from pathlib import Path
from datetime import datetime

TODO_FILE = Path(__file__).parent.parent / "todos.json"


def _load() -> list[dict]:
    if not TODO_FILE.exists():
        return []
    return json.loads(TODO_FILE.read_text())


def _save(todos: list[dict]) -> None:
    TODO_FILE.write_text(json.dumps(todos, indent=2))


def add_todo(title: str, priority: str = "medium") -> dict:
    """
    Add a new todo item.
    Priority: 'low' | 'medium' | 'high'
    """
    todos = _load()
    new_id = max((t["id"] for t in todos), default=0) + 1
    todo = {
        "id": new_id,
        "title": title,
        "priority": priority,
        "done": False,
        "created_at": datetime.now().isoformat(),
    }
    todos.append(todo)
    _save(todos)
    return {"message": f"Todo #{new_id} added ✅", "todo": todo}


def list_todos(filter_done: bool | None = None) -> dict:
    """
    List all todos.
    filter_done=True  → only completed
    filter_done=False → only pending
    filter_done=None  → all
    """
    todos = _load()
    if filter_done is not None:
        todos = [t for t in todos if t["done"] == filter_done]
    return {
        "total": len(todos),
        "todos": sorted(todos, key=lambda t: {"high": 0, "medium": 1, "low": 2}[t["priority"]]),
    }


def complete_todo(todo_id: int) -> dict:
    """Mark a todo as completed by its ID."""
    todos = _load()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            todo["completed_at"] = datetime.now().isoformat()
            _save(todos)
            return {"message": f"Todo #{todo_id} marked as done 🎉", "todo": todo}
    return {"error": f"Todo #{todo_id} not found"}


def delete_todo(todo_id: int) -> dict:
    """Delete a todo by its ID."""
    todos = _load()
    new_todos = [t for t in todos if t["id"] != todo_id]
    if len(new_todos) == len(todos):
        return {"error": f"Todo #{todo_id} not found"}
    _save(new_todos)
    return {"message": f"Todo #{todo_id} deleted 🗑️"}


def clear_completed() -> dict:
    """Remove all completed todos."""
    todos = _load()
    pending = [t for t in todos if not t["done"]]
    removed = len(todos) - len(pending)
    _save(pending)
    return {"message": f"Cleared {removed} completed todo(s)"}
