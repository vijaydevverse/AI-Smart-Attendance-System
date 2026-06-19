import sqlite3
from app.config import DATABASE_PATH

student_id = "STD-e5c64a7e"

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# Delete attendance
cursor.execute("DELETE FROM attendance WHERE student_id=?", (student_id,))
print("Attendance deleted:", cursor.rowcount)

# Delete face image records
cursor.execute("DELETE FROM face_images WHERE student_id=?", (student_id,))
print("Face images deleted:", cursor.rowcount)

# Delete embeddings
cursor.execute("DELETE FROM face_embeddings WHERE student_id=?", (student_id,))
print("Embeddings deleted:", cursor.rowcount)

# Delete student record
cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
print("Student deleted:", cursor.rowcount)

conn.commit()
conn.close()

print("✅ Vijay deleted successfully")