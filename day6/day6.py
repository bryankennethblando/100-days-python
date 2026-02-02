# Fucntion or class in java
def student(name: str):
    print(f"My student - {name}")

student("Bryan")

# function in a for looop
student_list = []
def students(number : int):
    for i in range(number):
        stundent_input = input("Student name: ")
        student_list.append(stundent_input)

students(5)
for i in range(5):
        print (f"My student number {i} {student_list[i]}")