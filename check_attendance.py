import sqlite3
from app.config import DATABASE_PATH

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

cursor.execute("SELECT * FROM attendance")
rows = cursor.fetchall()

print("Total rows:", len(rows))
print(rows)

conn.close()