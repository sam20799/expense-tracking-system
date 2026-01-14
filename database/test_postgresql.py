import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

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
