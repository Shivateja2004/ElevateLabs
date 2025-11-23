TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(TASK_FILE, "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        open(TASK_FILE, "w").close()  # create file if missing
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def remove_task(tasks):
    view_tasks(tasks)
    num = int(input("Enter task number to remove: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task removed.")
    else:
        print("Invalid number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- Your Tasks ---")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO MENU ---")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
