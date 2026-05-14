import sqlite3
from pathlib import Path

DB_PATH = Path("data/university.db")

def create_database():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.executescript("""
    DROP TABLE IF EXISTS enrollments;
    DROP TABLE IF EXISTS students;
    DROP TABLE IF EXISTS courses;
    DROP TABLE IF EXISTS majors;

    CREATE TABLE majors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );

    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        major_id INTEGER,
        FOREIGN KEY (major_id) REFERENCES majors(id)
    );

    CREATE TABLE courses (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        credits INTEGER NOT NULL,
        major_id INTEGER,
        FOREIGN KEY (major_id) REFERENCES majors(id)
    );

    CREATE TABLE enrollments (
        student_id INTEGER,
        course_id INTEGER,
        grade REAL,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    );
    """)

    majors = [
        (1, "Computer Science"),
        (2, "Economics"),
        (3, "Mathematics")
    ]

    students = [
        (1, "Alice", 21, 1),
        (2, "Bob", 19, 2),
        (3, "Charlie", 22, 1),
        (4, "Diana", 20, 3)
    ]

    courses = [
        (1, "Databases", 6, 1),
        (2, "Machine Learning", 6, 1),
        (3, "Microeconomics", 5, 2),
        (4, "Linear Algebra", 6, 3)
    ]

    enrollments = [
        (1, 1, 8.5),
        (1, 2, 9.0),
        (2, 3, 7.0),
        (3, 1, 6.5),
        (4, 4, 8.0)
    ]

    cursor.executemany("INSERT INTO majors VALUES (?, ?)", majors)
    cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students)
    cursor.executemany("INSERT INTO courses VALUES (?, ?, ?, ?)", courses)
    cursor.executemany("INSERT INTO enrollments VALUES (?, ?, ?)", enrollments)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()