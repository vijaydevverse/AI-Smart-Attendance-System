from app.database import get_connection

conn = get_connection()
cursor = conn.cursor()

columns = [
    ("photo_path", "TEXT"),
    ("exit_time", "TEXT")
]

for column_name, column_type in columns:
    try:
        cursor.execute(f"""
        ALTER TABLE attendance
        ADD COLUMN {column_name} {column_type}
        """)
        print(f"{column_name} column added successfully")
    except Exception as e:
        print(f"{column_name} update skipped:", e)

conn.commit()
conn.close()