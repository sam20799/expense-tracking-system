import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from .logging_setup import log_setup
import os
from dotenv import load_dotenv

load_dotenv()

logger = log_setup('db_helper')

DATABASE_URL = os.getenv("DATABASE_URL")

@contextmanager
def get_cursor(commit=False):
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor(cursor_factory=RealDictCursor)

    try:
        logger.info("Connected to PostgreSQL")
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


def fetch_expense_for_date(expense_date):
    logger.info(f'fetch_expense_for_date called with date: {expense_date}')
    with get_cursor() as cursor:
        cursor.execute(
            "SELECT * FROM expenses WHERE expense_date = %s",
            (expense_date,)
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
            VALUES (%s, %s, %s, %s)
            """,
            (expense_date, amount, category, notes)
        )


def delete_record(expense_date):
    logger.info('delete_record called')
    with get_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )
    print(f"Record deleted for date: {expense_date}")


def get_summary(start_date, end_date):
    logger.info(f'get_summary called with start_date: {start_date}, end_date: {end_date}')
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
            """,
            (start_date, end_date)
        )
        rows = cursor.fetchall()
        return rows_to_dict_list(rows)


def get_monthly_summary():
    logger.info('get_monthly_summary called')
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT 
                EXTRACT(MONTH FROM expense_date)::INT AS month_no,
                TO_CHAR(expense_date, 'Month') AS month_name,
                SUM(amount) AS total
            FROM expenses
            GROUP BY month_no, month_name
            ORDER BY month_no;
            """
        )
        rows = cursor.fetchall()
        return rows_to_dict_list(rows)


if __name__ == "__main__":
    expenses = fetch_expense_for_date('2025-08-15')
    print(expenses)

    summary = get_summary('2025-08-01', '2025-08-05')
    for record in summary:
        print(record)

    monthly_summary = get_monthly_summary()
    print(monthly_summary)
