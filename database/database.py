import sqlite3


conn = sqlite3.connect("student.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

conn.commit()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    department TEXT,
    cgpa REAL,
    attendance INTEGER
)
""")

conn.commit()

def insert_student(name, age, gender, department, cgpa, attendance):
    cursor.execute("""
    INSERT INTO students
    (name, age, gender, department, cgpa, attendance)
    VALUES (?,?,?,?,?,?)
    """, (name, age, gender, department, cgpa, attendance))

    conn.commit()

def view_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()