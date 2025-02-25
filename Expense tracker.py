import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """Load expenses from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        """Save expenses to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        """Add a new expense with amount, category, and description."""
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive.")

            expense = {
                "amount": amount,
                "category": category,
                "description": description,
                "date": datetime.now().strftime("%Y-%m-%d")
            }

            self.expenses.append(expense)
            self.save_expenses()
            print("Expense added successfully!")

        except ValueError as e:
            print(f"Error: {e}")

    def view_expenses(self):
        """Display all recorded expenses."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        for expense in self.expenses:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}, Date: {expense['date']}")

    def monthly_summary(self):
        """Provide a summary of expenses by month."""
        monthly_total = {}
        for expense in self.expenses:
            month = expense['date'][:7]
            monthly_total[month] = monthly_total.get(month, 0) + expense['amount']

        print("\nMonthly Summary:")
        for month, total in monthly_total.items():
            print(f"{month}: ${total:.2f}")

    def category_summary(self):
        """Provide a summary of expenses by category."""
        category_total = {}
        for expense in self.expenses:
            category = expense['category']
            category_total[category] = category_total.get(category, 0) + expense['amount']

        print("\nCategory-wise Summary:")
        for category, total in category_total.items():
            print(f"{category}: ${total:.2f}")

    def run(self):
        """Run the Expense Tracker user interface."""
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Monthly Summary")
            print("4. Category Summary")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                amount = input("Enter amount: ")
                category = input("Enter category (e.g., Food, Transport, Entertainment): ")
                description = input("Enter description: ")
                self.add_expense(amount, category, description)

            elif choice == '2':
                self.view_expenses()

            elif choice == '3':
                self.monthly_summary()

            elif choice == '4':
                self.category_summary()

            elif choice == '5':
                print("Exiting Expense Tracker. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
