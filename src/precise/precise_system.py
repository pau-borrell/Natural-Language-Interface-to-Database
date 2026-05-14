from src.precise.preprocessing import normalize_question
from src.precise.matcher import analyze_question
from src.precise.query_builder import build_sql

def compute_confidence(analysis):
    score = 0

    if analysis["table"]:
        score += 0.4

    if analysis["columns"]:
        score += 0.2

    if analysis["values"]:
        score += 0.15

    if analysis["numbers"]:
        score += 0.1

    if analysis["operator"]:
        score += 0.1

    if analysis["aggregation"]:
        score += 0.15

    return round(min(score, 1), 2)

class PreciseNL2SQL:
    def generate_sql(self, question):
        normalized_question = normalize_question(question)
        analysis = analyze_question(normalized_question)
        sql = build_sql(analysis)
        confidence = compute_confidence(analysis)

        return {
            "question": question,
            "normalized_question": normalized_question,
            "analysis": analysis,
            "sql": sql,
            "confidence": confidence
        }