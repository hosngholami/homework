from hossein_gholami_hw5.src.insert_student import insert_student
from hossein_gholami_hw5.src.write import write_file
from hossein_gholami_hw5.src.load_student import load_student
from hossein_gholami_hw5.src.display_student import display_student
from hossein_gholami_hw5.model.student import Student
from hossein_gholami_hw5.error_message.status_grade_error import StatusGradeError
from hossein_gholami_hw5.src.display_opration import display_opration
import json


def student_menu() -> None:

    oprations = {
        -1: 'exit',
        1: 'display student',
        2: 'insert student',
        3: 'write student',
        4: 'pick lecture'
        
    }

    display_opration(oprations)

    while True:
        op = int(input('student -> enter opration: '))
        match op:
            case 1:
                data = load_student()
                display_student(data)
            case 2:
                list_student = insert_student()
            case 3:
                try:
                    write_file('/hossein_gholami_hw5/data/student.json', file=json.dumps(list_student))
                except UnboundLocalError as ul:
                    print('please insert student')
            

            case 4:
                try:
                    student_id = input('please enter student id: ')
                    student = Student(student_id)
                    student.check_status()
                    if student.status == False:
                        raise StatusGradeError()
                    
                    student.pick_lecture()
                    student.update()                        
                except StatusGradeError as sge:
                    print(sge)
                except AttributeError as ab:
                    print('Student not found')

            case -1:
                break