import csv
import datetime

class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category
        self.date = datetime.date.today()

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def load_expenses(self):
        try:
            with open('expenses.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expense = Expense(float(row['amount']), row['category'])
                    expense.date = datetime.datetime.strptime(row['date'], '%Y-%m-%d').date()
                    self.expenses.append(expense)
        except FileNotFoundError:
            pass

    def save_expenses(self):
        with open('expenses.csv', 'w', newline='') as file:
            fieldnames = ['amount', 'category', 'date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow({'amount': expense.amount, 'category': expense.category, 'date': expense.date.strftime('%Y-%m-%d')})

    def add_expense(self):
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        new_expense = Expense(amount, category)
        self.expenses.append(new_expense)
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses yet.")
        else:
            for expense in self.expenses:
                print(f"Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}")

    def run(self):
        self.load_expenses()
        while True:
            print("\n1. Add Expense")
            print("2. View Expenses")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_expense()
                self.save_expenses()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
    