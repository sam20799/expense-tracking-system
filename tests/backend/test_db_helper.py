from backend import db_helper

def test_fetch_expenses_for_valid_date():
    expenses = db_helper.fetch_expense_for_date('2024-08-15')
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10
    assert expenses[0]['category'] == 'Shopping'
    assert expenses[0]['notes'] == 'Bought potatoes'

def test_fetch_expenses_for_invalid_date():
    expenses = db_helper.fetch_expense_for_date('9999-08-15')
    assert len(expenses) == 0

def test_fetch_expenses_summary_for_invalid_date():
    expenses = db_helper.fetch_expense_summary("9999-08-15", '2099-01-30')
    assert len(expenses) == 0

