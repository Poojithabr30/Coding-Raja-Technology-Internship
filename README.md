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
            priority = input("Enter priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_manager.add_task(title, priority, due_date)
            print("Task added successfully!")

        elif choice == "2":
            task_manager.list_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            task_manager.remove_task(index)
            print("Task removed successfully!")

        elif choice == "3":
            task_manager.list_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            task_manager.mark_task_completed(index)
            print("Task marked as completed!")

        elif choice == "4":
            task_manager.list_tasks()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()







import json

def main():
    transactions = load_transactions()
    while True:
        print("1. Add transaction")
        print("2. View remaining budget")
        print("3. View expense analysis")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_budget(transactions)
        elif choice == "3":
            view_expense_analysis(transactions)
        elif choice == "4":
            save_transactions(transactions)
            break
        else:
            print("Invalid choice. Please try again.")

def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"income": 0, "expenses": []}

def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)

def add_transaction(transactions):
    category = input("Enter transaction category: ")
    amount = float(input("Enter transaction amount: "))
    transaction_type = input("Enter transaction type (income/expense): ")
    
    if transaction_type.lower() == "income":
        transactions["income"] += amount
    elif transaction_type.lower() == "expense":
        transactions["expenses"].append({"category": category, "amount": amount})
        transactions["income"] -= amount
    else:
        print("Invalid transaction type.")

def view_budget(transactions):
    remaining_budget = transactions["income"]
    for expense in transactions["expenses"]:
        remaining_budget -= expense["amount"]
    print(f"Remaining budget: {remaining_budget}")

def view_expense_analysis(transactions):
    categories = {}
    for expense in transactions["expenses"]:
        category = expense["category"]
        if category in categories:
            categories[category] += expense["amount"]
        else:
            categories[category] = expense["amount"]
    
    print("Expense analysis:")
    for category, amount in categories.items():
        print(f"{category}: {amount}")

if __name__ == "__main__":
    main()
