import os
import psycopg2
from psycopg2.extras import execute_values
from datetime import date
from dotenv import load_dotenv

load_dotenv()

# Use environment variable DATABASE_URL or fallback to local
DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Create expenses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    expense_date DATE NOT NULL,
    amount FLOAT NOT NULL,
    category TEXT NOT NULL,
    notes TEXT
)
""")

# Insert initial data
data = [
    (3,'2025-08-02',180,'Food','Groceries and vegetables'),
    (4,'2025-08-02',120,'Other','Auto & bus fare'),
    (5,'2025-08-03',90,'Food','Lunch outside'),
    (11,'2025-08-02',60,'Other','Mobile recharge'),
    (12,'2025-08-02',250,'Other','Electricity bill'),
    (13,'2025-08-02',220,'Shopping','Household items'),
    (14,'2025-08-02',70,'Other','Tea & snacks'),
    (15,'2025-08-03',140,'Food','Dinner'),
    (16,'2025-08-03',50,'Entertainment','YouTube subscription'),
    (17,'2025-08-03',350,'Shopping','Clothing'),
    (18,'2025-08-03',40,'Other','Coffee'),
    (19,'2025-08-04',85,'Food','Lunch'),
    (20,'2025-08-04',300,'Shopping','Grocery refill'),
    (21,'2025-08-04',30,'Other','Parking'),
    (22,'2025-08-05',8500,'Rent','Monthly house rent'),
    (23,'2025-08-05',60,'Food','Snacks'),
    (24,'2025-08-05',120,'Entertainment','Movie'),
    (25,'2025-08-05',180,'Shopping','Books'),
    (26,'2025-08-05',35,'Other','Miscellaneous'),
    (27,'2025-08-06',70,'Food','Breakfast'),
    (28,'2025-08-06',220,'Shopping','Footwear'),
    (29,'2025-08-06',90,'Entertainment','Cinema'),
    (30,'2025-08-06',40,'Other','Bus fare'),
    (31,'2025-09-01',8500,'Rent','Monthly house rent'),
    (32,'2025-09-01',650,'Food','Weekly groceries'),
    (33,'2025-09-01',90,'Entertainment','Movie'),
    (34,'2025-09-01',300,'Shopping','Clothing'),
    (35,'2025-09-01',60,'Other','Bus & auto'),
    (36,'2025-09-02',500,'Food','Groceries'),
    (37,'2025-09-02',120,'Entertainment','Streaming subscription'),
    (38,'2025-09-02',200,'Shopping','Daily essentials'),
    (39,'2025-09-02',100,'Other','Fuel'),
    (40,'2025-09-03',150,'Food','Dinner'),
    (41,'2025-09-03',40,'Entertainment','Mobile game recharge'),
    (42,'2025-09-03',280,'Shopping','Accessories'),
    (43,'2025-09-03',35,'Other','Tea'),
    (44,'2025-09-04',90,'Food','Lunch'),
    (45,'2025-09-04',350,'Shopping','Grocery refill'),
    (46,'2025-09-04',25,'Other','Parking'),
    (47,'2025-09-05',1200,'Other','Internet & electricity'),
    (48,'2025-09-05',75,'Food','Snacks'),
    (49,'2025-09-05',150,'Entertainment','Movie'),
    (50,'2025-09-05',200,'Shopping','Stationery'),
    (51,'2025-09-05',40,'Other','Miscellaneous'),
    (52,'2025-09-30',700,'Food','Monthly groceries'),
    (53,'2025-09-30',120,'Entertainment','OTT subscription'),
    (54,'2025-09-30',350,'Shopping','Clothes'),
    (55,'2025-09-30',80,'Other','Bus pass'),
    (56,'2025-09-30',150,'Food','Dinner outside'),
    (62,'2025-08-15',45,'Food','Vegetables'),
    (63,'2025-08-01',600,'Food','Groceries'),
    (64,'2025-08-01',1200,'Other','Electricity bill'),
    (65,'2025-08-01',300,'Shopping','Monthly household items'),
    (66,'2025-08-01',500,'Food','Weekly groceries')
]

execute_values(cursor,
    "INSERT INTO expenses (id, expense_date, amount, category, notes) VALUES %s ON CONFLICT (id) DO NOTHING",
    data
)

conn.commit()
cursor.close()
conn.close()

print("PostgreSQL database and table created successfully!")
