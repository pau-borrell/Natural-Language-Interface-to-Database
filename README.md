# Natural Language Interface to Database

This project implements a Natural Language to SQL system. The goal is to translate English questions into SQL queries, execute them on a SQLite database, and return the results.

The project compares two approaches:

1. A rule-based PRECISE-inspired approach.
2. A machine-learning DBPal-inspired approach.

---

## Problem Statement

Natural Language Interfaces to Databases allow users to ask questions in ordinary language instead of writing SQL manually.

For example:

```text
Show students older than 20
```

is translated into:

```sql
SELECT * FROM students WHERE age > 20;
```

The problem is challenging because natural language is ambiguous, while SQL requires a precise structure.

---

## Technologies Used

- Python
- SQLite
- pytest

---

## Project Structure

```text
Natural-Language-Interface-to-Database/
│
├── data/
│   └── university.db
│
├── src/
│   ├── database/
│   │   ├── create_db.py
│   │   └── db_utils.py
│   │
│   ├── precise/
│   │   ├── schema.py
│   │   ├── lexicon.py
│   │   ├── preprocessing.py
│   │   ├── matcher.py
│   │   ├── query_builder.py
│   │   └── precise_system.py
│   │
│   └── main.py
│
├── tests/
│   └── test_precise.py
│
├── requirements.txt
└── README.md
```

---

## Database

The project uses a small SQLite university database.

The database contains the following tables:

### students

Stores student information.

| Column | Description |
|---|---|
| id | Student identifier |
| name | Student name |
| age | Student age |
| major_id | Reference to the student's major |

### majors

Stores university majors.

| Column | Description |
|---|---|
| id | Major identifier |
| name | Major name |

### courses

Stores course information.

| Column | Description |
|---|---|
| id | Course identifier |
| name | Course name |
| credits | Number of course credits |
| major_id | Reference to the related major |

### enrollments

Stores student-course enrollments and grades.

| Column | Description |
|---|---|
| student_id | Reference to the student |
| course_id | Reference to the course |
| grade | Student grade |

---

## PRECISE-Inspired Rule-Based Approach

The PRECISE-inspired system translates natural language questions into SQL using manually defined rules.

The system follows this pipeline:

```text
Natural language question
        ↓
Preprocessing
        ↓
Lexicon matching
        ↓
Schema element detection
        ↓
SQL template generation
        ↓
SQL execution
        ↓
Result
```

The system detects:

- tables
- columns
- values
- numbers
- operators
- aggregation functions

For example, the question:

```text
Show students older than 20
```

is analyzed as:

```text
table: students
column: age
operator: >
number: 20
```

and translated into:

```sql
SELECT * FROM students WHERE age > 20;
```

---

## Supported Query Types

The PRECISE-inspired system currently supports the following types of queries.

### Simple table queries

```text
Show all students
List all courses
```

Example output:

```sql
SELECT * FROM students;
```

### Numeric filtering

```text
Show students older than 20
What courses have more than 5 credits?
```

Example output:

```sql
SELECT * FROM students WHERE age > 20;
```

### Column selection

```text
Show student names
```

Example output:

```sql
SELECT name FROM students;
```

### Aggregation

```text
How many students are there?
What is the average grade of Alice?
What is the highest grade?
What is the lowest grade?
```

Example output:

```sql
SELECT COUNT(*) FROM students;
```

### Join queries

```text
Show students from Computer Science
```

Example output:

```sql
SELECT students.*
FROM students
JOIN majors ON students.major_id = majors.id
WHERE LOWER(majors.name) = 'computer science';
```

---

## Confidence Score

The system also returns a confidence score based on how many elements of the question were detected.

The score considers whether the system found:

- a table
- columns
- values
- numbers
- operators
- aggregation functions

This makes the rule-based system easier to interpret and debug.

---

## Evaluation

The system is evaluated in two ways:

1. SQL correctness: whether the generated SQL has the expected structure.
2. Execution correctness: whether the generated SQL returns the correct result from the database.

The tests are implemented with `pytest`.

---

## How to Run

First, create the database:

```powershell
python -m src.database.create_db
```

Then run the demo:

```powershell
python -m src.main
```

To run the tests:

```powershell
$env:PYTHONPATH="."; pytest
```

---

## Example Questions

```text
Show all students
List all courses
Show students older than 20
What courses have more than 5 credits?
Show students from Computer Science
What is the average grade of Alice?
How many students are there?
Show student names
What is the highest grade?
What is the lowest grade?
```

---

## Limitations

The PRECISE-inspired approach is simple, interpretable, and easy to debug. However, it has limited flexibility.

The system can only understand questions that match the vocabulary and templates defined in the lexicon and query builder. It may fail with complex questions, ambiguous language, or paraphrases that were not manually added.

This limitation is expected in rule-based systems and motivates the comparison with the DBPal-inspired machine-learning approach.

---

## Original Contribution

### Pau Borrell

My contribution was the implementation of the rule-based PRECISE-inspired NL2SQL system.

I implemented:

- the SQLite database creation script;
- the database schema representation;
- the lexicon mapping natural language expressions to database elements;
- question preprocessing;
- table, column, value, operator, number, and aggregation matching;
- SQL generation using predefined templates;
- join generation using foreign-key information;
- execution of generated SQL queries;
- confidence scoring;
- test cases for SQL correctness and execution correctness.

This part of the project is separated from the DBPal-inspired approach so that both systems can later be compared using the same database and evaluation questions.
