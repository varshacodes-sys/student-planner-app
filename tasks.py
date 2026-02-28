tasks = []

def add_task():
    name = input("Task name: ")
    due = input("Due date: ")
    tasks.append({"name": name, "due": due})
    print("Task added!")

def view_tasks():
    for t in tasks:
        print(f"{t['name']} - Due: {t['due']}")