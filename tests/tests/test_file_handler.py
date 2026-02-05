from finance_tracker.file_handler import load_expenses

def test_load_expenses():
    expenses = load_expenses()
    assert isinstance(expenses, list)
