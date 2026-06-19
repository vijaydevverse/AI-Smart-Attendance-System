# 🎓 AI Smart Attendance System

An AI-powered smart attendance system that uses **face recognition** to automatically mark student attendance with **Check-In / Check-Out tracking**, photo capture, voice feedback, and a real-time Streamlit dashboard.

---

## 🚀 Features

- ✅ Face registration for students  
- ✅ Face recognition using DeepFace + FaceNet512  
- ✅ Automatic attendance marking  
- ✅ Check-In / Check-Out system  
- ✅ Voice feedback (attendance confirmation via speaker)  
- ✅ Attendance photo capture  
- ✅ Streamlit dashboard for monitoring  
- ✅ Duplicate attendance prevention  
- ✅ Unknown face detection  
- ✅ SQLite database storage  

---

## 📌 Attendance Flow

### 🟢 Morning Check-In

When a student enters:

- Camera opens  
- Face is detected  
- Identity is recognized  
- Attendance is marked as **Checked IN**

**Example:**

| Name  | Date       | IN Time | OUT Time | Status     |
|-------|------------|---------|----------|------------|
| Vijay | 2026-06-19 | 09:10   | NULL     | Checked IN |

---

### 🔴 Evening Check-Out

When the same student leaves:

- Camera opens again  
- Face is recognized  
- OUT time is updated  

**Example:**

| Name  | Date       | IN Time | OUT Time | Status      |
|-------|------------|---------|----------|-------------|
| Vijay | 2026-06-19 | 09:10   | 16:25    | Checked OUT |

---

### ⚠️ Third Scan Same Day

If scanned again:

```

Already Checked Out

```

---

## 🧠 AI Technologies Used

- DeepFace  
- FaceNet512 Embeddings  
- OpenCV  
- Cosine Similarity Matching  
- Text-to-Speech (pyttsx3)  

---

## 🛠 Tech Stack

- Python  
- OpenCV  
- DeepFace  
- TensorFlow  
- SQLite  
- Streamlit  
- Pandas  
- Pillow  
- pyttsx3  

---

## 📂 Project Structure

```

AI-Smart-Attendance-System/
│
├── app/
│   ├── attendance.py
│   ├── config.py
│   ├── database.py
│   ├── embeddings.py
│   ├── matcher.py
│   ├── recognize.py
│   ├── register.py
│   ├── speaker.py
│   ├── train.py
│   └── utils.py
│
├── data/
│   ├── attendance_photos/
│   ├── exports/
│   └── attendance.db
│
├── main.py
├── init_db.py
├── streamlit_dashboard.py
├── requirements.txt
└── README.md

````

---

## ⚙ Installation

### Clone repository
```bash
git clone https://github.com/vijaydevverse/AI-Smart-Attendance-System
cd AI-Smart-Attendance-System
````

### Create virtual environment

```bash
python -m venv venv
```

### Activate environment (Windows)

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Setup Database

```bash
python init_db.py
```

---

## 👤 Register Student

```bash
python app/register.py
```

Stores:

* Student Name
* Roll Number
* Department
* Face Images

---

## 🧬 Train Face Embeddings

```bash
python -m app.train
```

---

## 🎥 Run Attendance System

```bash
python main.py
```

System will:

* Open webcam
* Detect face
* Match student
* Mark attendance
* Capture attendance photo
* Give voice confirmation

**Example output:**

```
Vijay - Checked IN  
Vijay - Checked OUT  
```

---

## 📊 Streamlit Dashboard

```bash
streamlit run streamlit_dashboard.py
```

Shows:

* Student details
* Attendance logs
* Check-in / Check-out time
* Status
* Attendance photos

---

## 🔊 Voice Feedback

System speaks:

* “Vijay, attendance checked in”
* “Vijay, attendance checked out”
* “Already checked out”

---

## 🔒 Smart Recognition Logic

* Face similarity threshold filtering
* Unknown face rejection
* Duplicate prevention
* One IN + one OUT per day

---

## 📈 Future Improvements

* Cloud database integration
* Admin dashboard login
* Attendance analytics
* Excel/CSV export
* Email notifications
* Multi-camera support

---

## 💡 Use Cases

* Colleges
* Schools
* Offices
* Training centers
* Labs
* Secure entry systems

---

## 👨‍💻 Author

**Vijay Krishnan P M**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub.

```
