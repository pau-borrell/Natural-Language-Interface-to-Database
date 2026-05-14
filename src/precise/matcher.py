import re
from src.precise.lexicon import (
    TABLE_SYNONYMS,
    COLUMN_SYNONYMS,
    VALUE_SYNONYMS,
    AGGREGATION_SYNONYMS,
    OPERATOR_SYNONYMS
)

def find_table(question):
    for table, synonyms in TABLE_SYNONYMS.items():
        for synonym in synonyms:
            if synonym in question:
                return table
    return None

def find_columns(question):
    columns = []
    for column, synonyms in COLUMN_SYNONYMS.items():
        for synonym in synonyms:
            if synonym in question:
                columns.append(column)
                break
    return columns

def find_values(question):
    values = []
    for value, synonyms in VALUE_SYNONYMS.items():
        for synonym in synonyms:
            if synonym in question:
                values.append(value)
                break
    return values

def find_numbers(question):
    return [int(number) for number in re.findall(r"\d+", question)]

def find_aggregation(question):
    for aggregation, synonyms in AGGREGATION_SYNONYMS.items():
        for synonym in synonyms:
            if synonym in question:
                return aggregation
    return None

def find_operator(question):
    for operator, synonyms in OPERATOR_SYNONYMS.items():
        for synonym in synonyms:
            if synonym in question:
                return operator
    return None

def infer_table_from_columns(columns):
    if "grade" in columns:
        return "enrollments"

    if "credits" in columns:
        return "courses"

    if "age" in columns:
        return "students"

    return None

def analyze_question(question):
    table = find_table(question)
    columns = find_columns(question)

    if table is None:
        table = infer_table_from_columns(columns)

    return {
        "table": table,
        "columns": columns,
        "values": find_values(question),
        "numbers": find_numbers(question),
        "aggregation": find_aggregation(question),
        "operator": find_operator(question)
    }