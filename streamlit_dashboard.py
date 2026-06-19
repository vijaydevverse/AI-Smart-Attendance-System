import streamlit as st
import sqlite3
import pandas as pd
import os
from PIL import Image
from app.config import DATABASE_PATH

st.set_page_config(page_title="Attendance Dashboard", layout="wide")
st.title("🎓 AI Smart Attendance Dashboard")

conn = sqlite3.connect(DATABASE_PATH)

query = """
SELECT
    students.full_name,
    students.roll_number,
    students.department,
    attendance.date,
    attendance.entry_time,
    attendance.exit_time,
    attendance.status,
    attendance.photo_path
FROM attendance
JOIN students
ON students.student_id = attendance.student_id
ORDER BY attendance.date DESC, attendance.entry_time DESC
"""

df = pd.read_sql(query, conn)
conn.close()

if df.empty:
    st.warning("No attendance records found")
else:
    st.dataframe(df, use_container_width=True)

    st.subheader("Attendance Cards")

    for _, row in df.iterrows():
        col1, col2 = st.columns([1, 3])

        with col1:
            if row["photo_path"] and os.path.exists(row["photo_path"]):
                image = Image.open(row["photo_path"])
                st.image(image, width=150)
            else:
                st.write("No Photo")

        with col2:
            st.write("### Student Info")
            st.write(f"Name: {row['full_name']}")
            st.write(f"Roll Number: {row['roll_number']}")
            st.write(f"Department: {row['department']}")
            st.write(f"Date: {row['date']}")
            st.write(f"Check IN: {row['entry_time']}")
            st.write(f"Check OUT: {row['exit_time']}")
            st.write(f"Status: {row['status']}")

        st.divider()