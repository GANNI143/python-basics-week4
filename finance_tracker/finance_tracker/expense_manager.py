from finance_tracker.expense import Expense
from finance_tracker.file_handler import load_expenses, save_expenses

class ExpenseManager:
    def add_expense(self, amount, category, description):
        expenses = load_expenses()
        expense = Expense(amount, category, description)
        expenses.append(expense.to_dict())
        save_expenses(expenses)

    def get_all_expenses(self):
        return load_expenses()
