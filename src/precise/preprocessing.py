import re

def normalize_question(question):
    question = question.lower().strip()
    question = re.sub(r"[^a-zA-Z0-9\s]", "", question)
    question = re.sub(r"\s+", " ", question)
    return question

def tokenize(question):
    return normalize_question(question).split()