import sqlite3
from app.config import DATABASE_PATH

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

cursor.execute("DELETE FROM attendance")

conn.commit()
conn.close()

print("Attendance cleared")