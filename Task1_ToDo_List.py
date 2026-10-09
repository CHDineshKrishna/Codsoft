"""
CODSOFT Python Programming Internship
Task 1: To-Do List Application

Features:
- Add a task
- View all tasks
- Update a task
- Mark a task as completed
- Delete a task
- Save tasks in a local JSON file
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load saved tasks, or return an empty list if no save file exists."""
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved tasks. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save the current task list to a JSON file."""
    DATA_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def view_tasks(tasks):
    """Display all tasks with their completion status."""
    print("\n========== YOUR TO-DO LIST ==========")
    if not tasks:
        print("No tasks yet. Add a task to get started.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. [{status}] {task['title']}")
    print("=====================================")


def add_task(tasks):
    """Ask the user for a task and add it to the list."""
    title = input("Enter the task: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")


def choose_task(tasks, prompt):
    """Return a zero-based task index, or None if the input is invalid."""
    if not tasks:
        print("Your to-do list is empty.")
        return None

    view_tasks(tasks)
    try:
        number = int(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None

    if not 1 <= number <= len(tasks):
        print("That task number does not exist.")
        return None
    return number - 1


def update_task(tasks):
    """Update the title of an existing task."""
    index = choose_task(tasks, "Enter the task number to update: ")
    if index is None:
        return

    new_title = input("Enter the new task title: ").strip()
    if not new_title:
        print("Task title cannot be empty.")
        return

    tasks[index]["title"] = new_title
    save_tasks(tasks)
    print("Task updated successfully.")


def mark_completed(tasks):
    """Mark a selected task as completed."""
    index = choose_task(tasks, "Enter the task number to mark completed: ")
    if index is None:
        return

    tasks[index]["completed"] = True
    save_tasks(tasks)
    print("Task marked as completed.")


def delete_task(tasks):
    """Delete a selected task."""
    index = choose_task(tasks, "Enter the task number to delete: ")
    if index is None:
        return

    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted task: {removed['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST MENU ==========")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Mark a task as completed")
        print("5. Delete a task")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Your tasks are saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
