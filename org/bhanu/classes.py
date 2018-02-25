students = []


class Student:    #pass  # To say py interpeter to do nothing
    def __init__(self, name, student_id=787):  # self refer to class from class , like this in java
        student = {"name": name, "student_id": student_id }
        students.append(student)

    def __str__(self):
        return "Student"


# With out constructor
#student = Student()
#student.add_student("Ben")
#print(students)

# With Constructor

mark = Student("Mark")

print(students)
print(mark)

# Class and instance attributes

