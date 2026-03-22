from datetime import datetime

def validate_task_title(title):
    # Requirement: Check for length
    if len(title.strip()) > 0:
        return True
    print("Error: Title cannot be empty.")
    return False

def validate_task_description(description):
    if len(description.strip()) > 0:
        return True
    print("Error: Description cannot be empty.")
    return False

def validate_due_date(due_date):
    try:
        # Check if format is YYYY-MM-DD
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        return False