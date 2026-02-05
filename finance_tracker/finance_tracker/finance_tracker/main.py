from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.reports import category_report

def main():
    manager = ExpenseManager()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Report")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            manager.add_expense(amount, category, description)
            print("Expense added!")

        elif choice == "2":
            expenses = manager.get_all_expenses()
            for e in expenses:
                print(e)

        elif choice == "3":
            expenses = manager.get_all_expenses()
            report = category_report(expenses)
            print(report)

        elif choice == "4":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
