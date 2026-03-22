from task_manager import validation

# Define tasks list
tasks = []

def add_task(title, description, due_date):
    # Use the validation functions before adding
    if (validation.validate_task_title(title) and 
        validation.validate_task_description(description) and 
        validation.validate_due_date(due_date)):
        
        new_task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        tasks.append(new_task)
        print("Task added successfully!")
    else:
        print("Task could not be added due to validation errors.")

def mark_task_as_complete(index, tasks=tasks):
    try:
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Error: Task index out of range.")
    except (ValueError, IndexError):
        print("Error: Invalid index.")

def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks!")
    else:
        print("\n--- Pending Tasks ---")
        for i, task in enumerate(tasks):
            if not task["completed"]:
                print(f"{i}. {task['title']} (Due: {task['due_date']})")

def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed_count = sum(1 for t in tasks if t["completed"])
    progress = (completed_count / len(tasks)) * 100
    return progress