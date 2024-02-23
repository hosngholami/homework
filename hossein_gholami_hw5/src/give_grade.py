from hossein_gholami_hw5.src.load_student import load_student
from hossein_gholami_hw5.model.student import Student

def give_grade():
    
    student = load_student()
    print(student)

    student_id = input('please enter student id: ')
    student_dict = student[student_id]

    student = Student()
