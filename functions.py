
tasks = []
PRIORITIES = ("high", "medium", "low")
id_counter = 1

def register_task(title, description, priority):
    global id_counter
    if priority not in PRIORITIES:
        return False, "Invalid priority, please enter a valid priority"
    
    new_task = {
        "id": id_counter,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "pending"
    }
    tasks.append(new_task)
    id_counter += 1
    return True, f"Task '{title}' registered with ID {new_task['id']}."

def get_all_tasks():
    return tasks

def search_by_criteria(criteria, value):
    results = []
    for t in tasks:
        if criteria == "id" and str(t["id"]) == str(value):
            results.append(t)
        elif criteria == "title" and value.lower() in t["title"].lower():
            results.append(t)
    return results

def update_task(task_id, new_title=None, new_status=None):
    for t in tasks:
        if t["id"] == task_id:
            if new_title: t["title"] = new_title
            if new_status: t["status"] = new_status
            return True
    return False

def delete_task(task_id):
    global tasks
    initial_length = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    return len(tasks) < initial_length