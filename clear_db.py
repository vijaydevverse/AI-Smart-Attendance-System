from app.database import get_connection

def clear_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM face_embeddings")

    conn.commit()
    conn.close()

    print("✅ Database cleared successfully!")

if __name__ == "__main__":
    clear_database()