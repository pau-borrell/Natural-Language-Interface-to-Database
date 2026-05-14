TABLE_SYNONYMS = {
    "students": ["student", "students", "person", "people", "pupil", "pupils", "learner", "learners"],
    "courses": ["course", "courses", "subject", "subjects", "class", "classes", "module", "modules"],
    "majors": ["major", "majors", "degree", "degrees", "program", "programs"],
    "enrollments": ["enrollment", "enrollments", "grades", "grade", "marks", "mark"]
}

COLUMN_SYNONYMS = {
    "name": ["name", "names", "called"],
    "age": ["age", "old", "older", "younger"],
    "credits": ["credit", "credits"],
    "grade": ["grade", "grades", "mark", "marks", "score", "scores"],
    "major_id": ["major", "degree", "program"],
    "id": ["id", "identifier"]
}

VALUE_SYNONYMS = {
    "computer science": ["computer science", "cs", "informatics"],
    "economics": ["economics", "econ"],
    "mathematics": ["mathematics", "math", "maths"],
    "alice": ["alice"],
    "bob": ["bob"],
    "charlie": ["charlie"],
    "diana": ["diana"]
}

AGGREGATION_SYNONYMS = {
    "count": ["how many", "number of", "count", "total number of"],
    "avg": ["average", "mean", "avg"],
    "max": ["maximum", "highest", "best", "largest"],
    "min": ["minimum", "lowest", "worst", "smallest"]
}

OPERATOR_SYNONYMS = {
    ">": ["older than", "greater than", "more than", "above", "higher than"],
    "<": ["younger than", "less than", "fewer than", "below", "lower than"],
    "=": ["equal to", "equals", "is", "are", "from", "in", "with"]
}