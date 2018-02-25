students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=787):
    student = {"name": name, "student_id": student_id }
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Can't open file ")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Can't read the file")


def var_args(name, **kwargs):  # * args , variable number of args
    print(name)
    #print(args)
    print(kwargs["wmsg"])

#students_list = get_students_titlecase()

read_file()
print_students_titlecase()
student_name="Marks"
add_student(student_name, 5565)
save_file(student_name)

#print_students_titlecase()

# var_args("ben", message="hello", id=888 , wmsg="welcome", istrue=True)

#student_name = input("Enter student name: ")
#student_id = input("Enter student ID : ")

#add_student(student_name, student_id)
print_students_titlecase()


#Lambda Functions "Anonymous functions"

#double = lambda x: x + 2

#double(5) == 7

