from tasks import add_task, view_tasks

while True:
    print("\nStudent Planner")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break