"""
Determine:

-> Average score per student.
-> Average score per subject.
-> Best student in each subject.
-> Best overall student.
-> Subjects where every student scored above 80.
-> Subjects where at least one student scored below 80.
-> Highest individual score.
-> All students who achieved that score.

Then create:
{
    "S001": {
        "name": "Amin",
        "overall_average": ...,
        "best_subject": ...,
        "subjects_above_85": {...}
    }
}

Focus: dictionary traversal several levels deep.
"""

students = {
    "S001": {
        "name": "Amin",
        "subjects": {"Python": [80, 85, 90], "SQL": [75, 80, 85], "Git": [90, 95, 88]},
    },
    "S002": {
        "name": "Nadia",
        "subjects": {"Python": [95, 90, 92], "SQL": [88, 85, 90], "Git": [80, 85, 82]},
    },
}

def grade_analysis(students:dict):
    pass


avarage_score = {}

for student_id, details in students.items():
    for subject, marks in students[student_id]["subjects"].items():
        avarage_score.setdefault(students[student_id]["name"], 0)
        avarage_score[students[student_id]["name"]] += sum(marks)

print(avarage_score)
