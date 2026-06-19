import sqlite3
import pandas as pd
from app.config import DATABASE_PATH

print("DB PATH:", DATABASE_PATH)

conn = sqlite3.connect(DATABASE_PATH)

query = """
SELECT
    students.full_name,
    students.roll_number,
    students.department,
    attendance.date,
    attendance.entry_time,
    attendance.status,
    attendance.photo_path
FROM attendance
JOIN students
ON students.student_id = attendance.student_id
ORDER BY attendance.date DESC, attendance.entry_time DESC
"""

df = pd.read_sql(query, conn)
conn.close()

print("\n===== ATTENDANCE DASHBOARD =====\n")
print(df)

if len(df) == 0:
    print("No attendance records found.")