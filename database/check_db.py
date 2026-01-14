import sqlite3
import pandas as pd
from pathlib import Path

db_path = Path(__file__).parent / "expenses.db"
conn = sqlite3.connect(db_path)

df = pd.read_sql_query("SELECT * FROM expenses", conn)

conn.close()

# put a breakpoint on print and run in debug mode and see ad df : better view
print(df)
