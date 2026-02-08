# finding and fixing bugs into this code

# 🚨 Don't change the code below 👇
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO: Create an empty dictionary called student_grades.
# student_grades = [] -- it's a list not a dict
student_grades = {}

# TODO: Write a loop that iterates through the student_scores dictionary
# and assigns a grade to student_grades for each student.

# first bug: for student in student_scores -- missing a colon
for student in student_scores:
    score = student_scores[student]
    
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
        
    student_grades[student] = grade
    

# 🚨 Don't change the code below 👇
print(student_grades)