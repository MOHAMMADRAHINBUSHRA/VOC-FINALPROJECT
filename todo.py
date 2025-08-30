
import json
import os

# ==============================
# Task Class to represent a Task
# ==============================
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False  # By default, task is not completed

    def mark_completed(self):
        """Mark the task as completed"""
        self.completed = True


# ==============================
# File Handling Functions
# ==============================
def save_tasks(tasks, filename="tasks.json"):
    """Save tasks to a JSON file"""
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)


def load_tasks(filename="tasks.json"):
    """Load tasks from a JSON file"""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            return [Task(**task) for task in data]
    return []


# ==============================
# Helper Functions
# ==============================
def add_task(tasks):
    """Add a new task"""
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (Work/Personal/Urgent): ")
    tasks.append(Task(title, description, category))
    print("✅ Task added successfully!")


def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("⚠️ No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task.completed else "❌ Not Completed"
        print(f"\nTask {i}:")
        print(f"  Title: {task.title}")
        print(f"  Description: {task.description}")
        print(f"  Category: {task.category}")
        print(f"  Status: {status}")


def mark_task_completed(tasks):
    """Mark a task as completed"""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        tasks[index].mark_completed()
        print("✅ Task marked as completed!")
    except (IndexError, ValueError):
        print("⚠️ Invalid input. Please try again.")


def delete_task(tasks):
    """Delete a task"""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        deleted = tasks.pop(index)
        print(f"🗑 Task '{deleted.title}' deleted successfully!")
    except (IndexError, ValueError):
        print("⚠️ Invalid input. Please try again.")


# ==============================
# Main Application Loop
# ==============================
def main():
    tasks = load_tasks()  # Load tasks at the start

    while True:
        print("\n========== Personal To-Do List ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        print("=========================================")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)  # Save tasks before exit
            print("💾 Tasks saved. Exiting application. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1-5.")


# ==============================
# Run the Application
# ==============================
if __name__ == "__main__":
    main()
