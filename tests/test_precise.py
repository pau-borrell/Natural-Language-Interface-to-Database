from src.precise.precise_system import PreciseNL2SQL
from src.database.db_utils import execute_sql

DB_PATH = "data/university.db"

def test_show_all_students():
    system = PreciseNL2SQL()
    output = system.generate_sql("Show all students")
    assert output["sql"] == "SELECT * FROM students;"

def test_count_students():
    system = PreciseNL2SQL()
    output = system.generate_sql("How many students are there?")
    assert output["sql"] == "SELECT COUNT(*) FROM students;"

def test_students_older_than_20():
    system = PreciseNL2SQL()
    output = system.generate_sql("Show students older than 20")
    assert output["sql"] == "SELECT * FROM students WHERE age > 20;"

def test_show_all_courses():
    system = PreciseNL2SQL()
    output = system.generate_sql("List all courses")
    assert output["sql"] == "SELECT * FROM courses;"

def test_courses_more_than_5_credits():
    system = PreciseNL2SQL()
    output = system.generate_sql("What courses have more than 5 credits?")
    assert output["sql"] == "SELECT * FROM courses WHERE credits > 5;"

def test_students_from_computer_science():
    system = PreciseNL2SQL()
    output = system.generate_sql("Show students from Computer Science")
    expected = """
SELECT students.*
FROM students
JOIN majors ON students.major_id = majors.id
WHERE LOWER(majors.name) = 'computer science';
""".strip()
    assert output["sql"] == expected

def test_average_grade_of_alice():
    system = PreciseNL2SQL()
    output = system.generate_sql("What is the average grade of Alice?")
    expected = """
SELECT AVG(enrollments.grade)
FROM enrollments
JOIN students ON enrollments.student_id = students.id
WHERE students.name = 'Alice';
""".strip()
    assert output["sql"] == expected

def test_select_student_names():
    system = PreciseNL2SQL()
    output = system.generate_sql("Show student names")
    assert output["sql"] == "SELECT name FROM students;"

def test_highest_grade():
    system = PreciseNL2SQL()
    output = system.generate_sql("What is the highest grade?")
    assert output["sql"] == "SELECT MAX(grade) FROM enrollments;"

def test_lowest_grade():
    system = PreciseNL2SQL()
    output = system.generate_sql("What is the lowest grade?")
    assert output["sql"] == "SELECT MIN(grade) FROM enrollments;"

def test_students_older_than_20_execution():
    system = PreciseNL2SQL()
    output = system.generate_sql("Show students older than 20")
    result = execute_sql(DB_PATH, output["sql"])

    rows = result["rows"]

    assert len(rows) == 2
    assert rows[0][1] == "Alice"
    assert rows[1][1] == "Charlie"

def test_count_students_execution():
    system = PreciseNL2SQL()
    output = system.generate_sql("How many students are there?")
    result = execute_sql(DB_PATH, output["sql"])

    assert result["rows"][0][0] == 4

def test_average_grade_of_alice_execution():
    system = PreciseNL2SQL()
    output = system.generate_sql("What is the average grade of Alice?")
    result = execute_sql(DB_PATH, output["sql"])

    assert result["rows"][0][0] == 8.75

def test_unknown_question():
    system = PreciseNL2SQL()
    output = system.generate_sql("Who is the best student?")
    assert output["sql"] is None

def test_confidence_exists():
    system = PreciseNL2SQL()
    output = system.generate_sql("Show students older than 20")
    assert "confidence" in output
    assert output["confidence"] > 0