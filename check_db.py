from app.database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(attendance)")
print(cursor.fetchall())

conn.close()