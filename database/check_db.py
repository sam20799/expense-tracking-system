import psycopg2
from psycopg2.extras import RealDictCursor  # optional, to get results as dicts
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

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


