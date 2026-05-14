from src.precise.precise_system import PreciseNL2SQL
from src.database.db_utils import execute_sql

DB_PATH = "data/university.db"

def main():
    system = PreciseNL2SQL()

    questions = [
        "Show all students",
        "List all courses",
        "Show students older than 20",
        "What courses have more than 5 credits?",
        "Show students from Computer Science",
        "What is the average grade of Alice?",
        "How many students are there?",
        "Show student names",
        "What is the highest grade?",
        "What is the lowest grade?",
        "Who is the best student?"
    ]

    for question in questions:
        output = system.generate_sql(question)

        print("=" * 80)
        print("Question:", output["question"])
        print("Normalized:", output["normalized_question"])
        print("Analysis:", output["analysis"])
        print("Confidence:", output["confidence"])
        print("SQL:", output["sql"])

        if output["sql"] is None:
            print("Result: Unsupported question")
        else:
            result = execute_sql(DB_PATH, output["sql"])
            print("Result:", result)

if __name__ == "__main__":
    main()