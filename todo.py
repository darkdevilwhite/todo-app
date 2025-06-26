# todo.py

TODO_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            if not tasks:
                print("No tasks found.")

        elif choice == "2":
            task = input("Enter a task: ")
            if task.strip():
                tasks.append(task.strip())
                save_tasks(tasks)
                print("Task added.")

        elif choice == "3":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
