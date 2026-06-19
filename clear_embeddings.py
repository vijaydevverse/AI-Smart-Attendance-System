from app.database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("DELETE FROM face_embeddings")
conn.commit()
conn.close()

print("Cleared old embeddings")