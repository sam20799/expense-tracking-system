import psycopg2
from psycopg2.extras import RealDictCursor  # optional, to get results as dicts
import os

DATABASE_URL = "postgresql://expenses_db_a5u5_user:W81hb8nLTx7PP884sobVCoC9nhaedMtK@dpg-d5jr9h7gi27c73e1mkfg-a.singapore-postgres.render.com/expenses_db_a5u5"

# Connect to DB
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor(cursor_factory=RealDictCursor)  # optional: get dict instead of tuple

# Execute SELECT query
cursor.execute("SELECT * FROM expenses")

# Fetch all rows
rows = cursor.fetchall()

# Print rows
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()


