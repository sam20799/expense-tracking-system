import sqlite3
from contextlib import contextmanager
from backend.logging_setup import log_setup
from pathlib import Path


logger = log_setup('db_helper')

DB_PATH = Path(__file__).parent / 'expenses.db'


@contextmanager
def get_cursor(commit=False):
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row  # <-- enables dict-like rows

    try:
        print("connected to sqlite")
        cursor = connection.cursor()
        yield cursor

        if commit:
            connection.commit()

    finally:
        cursor.close()
        connection.close()


def rows_to_dict_list(rows):
    return [dict(row) for row in rows]


def fetch_all_record():
    logger.info('fetch_all_record called')
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        return rows_to_dict_list(rows)


def fetch_expense_for_date(date):
    logger.info(f'fetch_expense_for_date called with date: {date}')
    with get_cursor() as cursor:
        cursor.execute(
            "SELECT * FROM expenses WHERE expense_date = ?",
            (date,)
        )
        rows = cursor.fetchall()
        return rows_to_dict_list(rows)


def insert_record(expense_date, amount, category, notes):
    logger.info(
        f'insert_record called with expense_date: {expense_date}, '
        f'amount: {amount}, category: {category}, notes: {notes}'
    )

    with get_cursor(commit=True) as cursor:
        cursor.execute(
            """
            INSERT INTO expenses (expense_date, amount, category, notes)
            VALUES (?, ?, ?, ?)
            """,
            (expense_date, amount, category, notes)
        )


def delete_record(expense_date):
    logger.info('delete_record called')

    with get_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date = ?",
            (expense_date,)
        )

    print(f"Record deleted for date: {expense_date}")


def get_summary(start_date, end_date):
    logger.info(
        f'get_summary called with start_date: {start_date}, end_date: {end_date}'
    )

    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            WHERE expense_date BETWEEN ? AND ?
            GROUP BY category
            """,
            (start_date, end_date)
        )

        rows = cursor.fetchall()
        return rows_to_dict_list(rows)


if __name__ == "__main__":
    expenses = fetch_expense_for_date('2025-08-15')
    print(expenses)

    summary = get_summary('2025-08-01', '2025-08-05')
    for record in summary:
        print(record)



