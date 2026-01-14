from backend import db_helper

def test_expense_for_date():
    expenses = db_helper.fetch_expense_for_date('2025-08-15')
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 45
    assert expenses[0]['category'] == 'Food'
    assert expenses[0]['notes'] == 'Vegetables'

def test_expenses_invalid_date():
    expenses = db_helper.fetch_expense_for_date('9999-08-15')

    assert len(expenses) == 0

def test_expenses_invalid_summary():
    expenses = db_helper.get_summary('2029-08-01', '2029-08-01')

    assert len(expenses) == 0
