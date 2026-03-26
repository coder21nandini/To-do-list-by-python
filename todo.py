import csv
import os

FILENAME = "todo.csv"

def add_task():
    task = input("Enter task description: ")
    status = "Pending"
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([task, status])
    print("Task added!")

def view_tasks():
    if not os.path.exists(FILENAME):
        print("No tasks found.")
        return

    print("\n--- To-Do List ---")
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        tasks = list(reader)

    if not tasks:
        print("No tasks in list.")
        return

    for idx, (task, status) in enumerate(tasks, 1):
        print(f"{idx}. {task} [{status}]")

def update_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to update: ")) - 1
    except ValueError:
        print("Invalid number.")
        return

    with open(FILENAME, "r") as f:
        tasks = list(csv.reader(f))

    if 0 <= task_num < len(tasks):
        new_task = input("Enter new task description: ")
        new_status = input("Enter new status (Pending/Done): ").capitalize()
        tasks[task_num] = [new_task, new_status]

        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(tasks)

        print("Task updated.")
    else:
        print("Task number out of range.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to delete: ")) - 1
    except ValueError:
        print("Invalid number.")
        return

    with open(FILENAME, "r") as f:
        tasks = list(csv.reader(f))

    if 0 <= task_num < len(tasks):
        del tasks[task_num]
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(tasks)
        print("Task deleted.")
    else:
        print("Task number out of range.")

def menu():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
