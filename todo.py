import json
import sys
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")

def load_tasks():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task.get("done") else "[ ]"
        print(f"{i}. {status} {task.get('description')}")

def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked task {index + 1} as done")
    except IndexError:
        print("Invalid task number")

def remove_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Removed task: {removed.get('description')}")
    except IndexError:
        print("Invalid task number")

def print_help():
    print("Usage:")
    print("  python todo.py add <description>")
    print("  python todo.py list")
    print("  python todo.py done <task number>")
    print("  python todo.py remove <task number>")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]
    if command == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done" and len(sys.argv) > 2 and sys.argv[2].isdigit():
        mark_done(int(sys.argv[2]) - 1)
    elif command == "remove" and len(sys.argv) > 2 and sys.argv[2].isdigit():
        remove_task(int(sys.argv[2]) - 1)
    else:
        print_help()
