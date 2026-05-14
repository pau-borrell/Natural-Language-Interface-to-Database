import sqlite3

def execute_sql(db_path, sql):
    if sql is None:
        return []

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    conn.close()

    return {
        "columns": column_names,
        "rows": rows
    }