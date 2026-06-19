from app.database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
SELECT student_id, full_name, roll_number
FROM students
WHERE full_name = ?
""", ("Vijay",))

print(cursor.fetchall())

conn.close()