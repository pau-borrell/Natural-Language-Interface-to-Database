SCHEMA = {
    "students": {
        "columns": ["id", "name", "age", "major_id"],
        "primary_key": "id"
    },
    "majors": {
        "columns": ["id", "name"],
        "primary_key": "id"
    },
    "courses": {
        "columns": ["id", "name", "credits", "major_id"],
        "primary_key": "id"
    },
    "enrollments": {
        "columns": ["student_id", "course_id", "grade"],
        "primary_key": None
    }
}

FOREIGN_KEYS = {
    ("students", "major_id"): ("majors", "id"),
    ("courses", "major_id"): ("majors", "id"),
    ("enrollments", "student_id"): ("students", "id"),
    ("enrollments", "course_id"): ("courses", "id")
}