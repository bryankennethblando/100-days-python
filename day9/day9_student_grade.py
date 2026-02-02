# evaluating the remarks of students in a dictionaries

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student, grade in student_scores.items():
    if grade > 90:
        student_grades[student] = "Outstanding"
    elif grade > 80:
        student_grades[student] = "Exceeds Expectations"
    elif grade > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student]= "Fail"

print(student_grades)