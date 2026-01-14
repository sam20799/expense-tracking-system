import os
import psycopg2

DATABASE_URL = "postgresql://expenses_db_a5u5_user:W81hb8nLTx7PP884sobVCoC9nhaedMtK@dpg-d5jr9h7gi27c73e1mkfg-a.singapore-postgres.render.com/expenses_db_a5u5"

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id SERIAL PRIMARY KEY,
        expense_date DATE NOT NULL,
        amount FLOAT NOT NULL,
        category TEXT NOT NULL,
        notes TEXT
    );
    """)

    conn.commit()
    cur.close()
    conn.close()


def get_connection():
    return psycopg2.connect(DATABASE_URL)

create_tables()
