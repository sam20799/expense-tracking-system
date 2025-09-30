import mysql.connector
from contextlib import contextmanager


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rootuser',
        database='expense_manager'
    )

    if connection.is_connected():
        print('database connected')
    else:
        print('database not connected')

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute('select * from expenses')
        expenses = cursor.fetchall()
        return expenses

def fetch_expense_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute('select * from expenses where expense_date= %s', (expense_date,))
        expenses = cursor.fetchall()
        return expenses

def insert_expense(exp_date,amount,category,notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute('''insert into expenses (expense_date,amount,category,notes)
                          values (%s,%s,%s,%s)''',(exp_date,amount,category,notes))
        print("Inserted expense record")

def delete_expense_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("delete from expenses where expense_date=%s",(expense_date,))
        print("Deleted expense record")

def fetch_expense_summary(start_date,end_date):
    with get_db_cursor() as cursor:
        cursor.execute('''select category,sum(amount) as total
                          from expenses
                          where expense_date between %s and %s
                          group by category''',(start_date,end_date))
        expenses = cursor.fetchall()
        return expenses
def fetch_monthly_expense(date):
    with get_db_cursor() as cursor:
        cursor.execute('''
                            SELECT 
                            DATE_FORMAT(expense_date, '%Y-%m') AS month,
                            SUM(amount) AS total_monthly_expense
                            FROM 
                            expenses
                            WHERE 
                            DATE_FORMAT(expense_date, '%Y-%m') = DATE_FORMAT('2024-08-20', '%Y-%m')
                            GROUP BY 
                            DATE_FORMAT(expense_date, '%Y-%m');
        ''', (date,))
        expenses = cursor.fetchall()
        print(expenses)

if __name__ == "__main__":
    # fetch_all_records()
    # fetch_expense_for_date("2024-08-02")
    # insert_expense("2024-08-20",300,"food","pizza")
    # fetch_expense_for_date("2024-08-20")
    # delete_expense_for_date("2024-08-30")
    # fetch_expense_for_date("2024-08-20")
    # fetch_expense_summary('2024-08-01','2024-08-05')
    fetch_monthly_expense('2024-08-20')


