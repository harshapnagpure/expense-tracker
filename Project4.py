import json
import os

FILE_NAME = "expenses.json"

# Load existing data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add expense
def add_expense(data):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (food, travel, etc.): ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    data.append(expense)
    save_data(data)
    print("Expense added successfully!")

# View expenses
def view_expenses(data):
    if not data:
        print("No expenses found.")
        return

    total = 0
    print("\n--- Expense List ---")
    for i, exp in enumerate(data, start=1):
        print(f"{i}. {exp['name']} - ₹{exp['amount']} ({exp['category']})")
        total += exp['amount']

    print(f"\nTotal Expense: ₹{total}")

# Main menu
def main():
    data = load_data()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()