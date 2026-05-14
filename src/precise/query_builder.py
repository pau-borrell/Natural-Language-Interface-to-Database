from src.precise.schema import FOREIGN_KEYS

def find_join_condition(table1, table2):
    for (source_table, source_column), (target_table, target_column) in FOREIGN_KEYS.items():
        if source_table == table1 and target_table == table2:
            return f"{table1}.{source_column} = {table2}.{target_column}"

        if source_table == table2 and target_table == table1:
            return f"{table2}.{source_column} = {table1}.{target_column}"

    return None

def build_sql(analysis):
    table = analysis["table"]
    columns = analysis["columns"]
    values = analysis["values"]
    numbers = analysis["numbers"]
    aggregation = analysis["aggregation"]
    operator = analysis["operator"]

    if table is None:
        return None

    if aggregation in ["max", "min"] and not columns:
        return None

    if aggregation == "count":
        return f"SELECT COUNT(*) FROM {table};"

    if aggregation == "avg" and "grade" in columns:
        if values:
            student_name = values[0].capitalize()
            join_condition = find_join_condition("enrollments", "students")
            return f"""
SELECT AVG(enrollments.grade)
FROM enrollments
JOIN students ON {join_condition}
WHERE students.name = '{student_name}';
""".strip()
        return "SELECT AVG(grade) FROM enrollments;"

    if aggregation == "max" and columns:
        return f"SELECT MAX({columns[0]}) FROM {table};"

    if aggregation == "min" and columns:
        return f"SELECT MIN({columns[0]}) FROM {table};"

    if table == "students" and "age" in columns and numbers and operator:
        return f"SELECT * FROM students WHERE age {operator} {numbers[0]};"

    if table == "courses" and "credits" in columns and numbers and operator:
        return f"SELECT * FROM courses WHERE credits {operator} {numbers[0]};"

    if table == "students" and values:
        value = values[0]

        if value in ["computer science", "economics", "mathematics"]:
            join_condition = find_join_condition("students", "majors")
            return f"""
SELECT students.*
FROM students
JOIN majors ON {join_condition}
WHERE LOWER(majors.name) = '{value}';
""".strip()

        return f"SELECT * FROM students WHERE LOWER(name) = '{value}';"

    if table == "courses" and values:
        value = values[0]

        if value in ["computer science", "economics", "mathematics"]:
            join_condition = find_join_condition("courses", "majors")
            return f"""
SELECT courses.*
FROM courses
JOIN majors ON {join_condition}
WHERE LOWER(majors.name) = '{value}';
""".strip()

    if table and columns and not numbers and not values and not aggregation:
        selected_columns = ", ".join(columns)
        return f"SELECT {selected_columns} FROM {table};"

    return f"SELECT * FROM {table};"