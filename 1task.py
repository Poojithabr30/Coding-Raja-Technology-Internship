import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, title, priority, due_date):
        self.tasks.append({"title": title, "priority": priority, "due_date": due_date, "completed": False})
        self.save_tasks()

    def remove_task(self, index):
        del self.tasks[index]
        self.save_tasks()

    def mark_task_completed(self, index):
        self.tasks[index]["completed"] = True
        self.save_tasks()

    def list_tasks(self):
        print("Tasks:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}. [{status}] {task['title']} (Priority: {task['priority']}, Due Date: {task['due_date']})")


def main():
    task_manager = TaskManager()
    task_manager.load_tasks()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Mark Task Completed\n4. List Tasks\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter priority (High/Medium/Low): ").lower()
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_manager.add_task(title, priority, due_date)
            print("Task added successfully!")

        elif choice == "2":
            task_manager.list_tasks()
            try:
                index = int(input("Enter task number to remove: ")) - 1
                task_manager.remove_task(index)
                print("Task removed successfully!")
            except ValueError:
                print("Invalid input! Please enter a valid task number.")

        elif choice == "3":
            task_manager.list_tasks()
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                task_manager.mark_task_completed(index)
                print("Task marked as completed!")
            except ValueError:
                print("Invalid input! Please enter a valid task number.")

        elif choice == "4":
            task_manager.list_tasks()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
