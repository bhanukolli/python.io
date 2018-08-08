students = []


class Student:    #pass  # To say py interpeter to do nothing

    school_name = "Nalanda school"
    def __init__(self, name, student_id=787):  # self refer to class from class , like this in java
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

class HighSchoolStudent(Student):

    school_name = "Nalanda college"

    def get_school_name(self):
        return "This is a High school"
    
    # def get_name_capitalize(self):
    #     original_value = super.get_name_capitalize()
    #     return original_value + "-HS"



james = HighSchoolStudent("james")

print(james.get_name_capitalize())
# Class and instance attributes

#mark = Student("Mark")

#print(students)
#print(mark)


print(Student.school_name)
print(james.get_school_name())

print("Hello")