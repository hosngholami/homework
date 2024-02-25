from hossein_gholami_hw5.src.insert_lecture import insert_lecture   
from hossein_gholami_hw5.src.write import write_file
from hossein_gholami_hw5.src.insert_student import insert_student
from hossein_gholami_hw5.src.load_student import load_student
from hossein_gholami_hw5.src.pick_lecture import pick_lecture
from hossein_gholami_hw5.model.student import Student
from hossein_gholami_hw5.error_message.status_grade_error import StatusGradeError
from hossein_gholami_hw5.src.insert_proffesor import insert_proffesor
from hossein_gholami_hw5.src.load_proffesor import load_proffesor
from hossein_gholami_hw5.src.load_lecture import load_lecture
from hossein_gholami_hw5.model.proffesor import Proffesor
from hossein_gholami_hw5.src.display_student import display_student
from hossein_gholami_hw5.error_message.lecture_error import LectureError
from hossein_gholami_hw5.src.display_proffesor import display_proffesor
from hossein_gholami_hw5.src.display_lecture import display_lectures
import json


def main():

    opration = {
        -1: 'exit',
        1: 'insert lecture',
        2: 'write lecture to file',
        3: 'insert student',
        4: 'write student to file',
        5: 'load student',
        6: 'grade lacture',
        7: 'insert proffesor',
        8: 'write proffesor to file',
        9: 'load proffesor',
        10: 'take lecture with proffesor',
        11: 'load lecture'
        
    }
    print('#### Help ######')
    print('enter -1 for save and exit on opration')
    print('if you can saved file, you should write to file')

    print('-------------------------')
    print('#### Condition ##### ')
    print("if student avg lower 12, can't take a lecture ")
    print("proffesor can't take lecture biger 3 ")

    print('---------------------------------')


    for key, value in opration.items():
        print(f'{value} -> {key}')

    print('---------------------------')
    while True:

            try:
                state = int(input('select opration: '))
            except ValueError as ve:
                print('input is invalid')

            else:
                match state:
                    case 1:
                        for key, value in load_lecture().items():
                            print(f'{key} : {value}')
                        lecture =  insert_lecture()
                    case 2:
                        write_file(file_name='/hossein_gholami_hw5/data/book.json', file=json.dumps(lecture))
                    case 3:
                        list_student = insert_student()
                    case 4:
                        try:
                            write_file('/hossein_gholami_hw5/data/student.json', file=json.dumps(list_student))
                        except UnboundLocalError as ul:
                            print('please insert student')
                    case 5:
                        data = load_student()
                        display_student(data)
                    case 6:
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

                    case 7:
                        proffesors = insert_proffesor()
                    case 8:
                        try:
                            write_file(file_name='/hossein_gholami_hw5/data/proffesor.json', file=json.dumps(proffesors))
                        except UnboundLocalError as ul:
                            print('please insert proffesor')
                    case 9:

                        proffesor = load_proffesor()
                        display_proffesor(proffesor)
                    case 10:
                        try:
                            proffesor_id = input('enter proffesor_number')
                            proffesor = Proffesor(proffesor_id)
                            proffesor.check_status()
                            if proffesor.status == False:
                                raise LectureError("proffesor can't give bigger 3 lecture")
                            proffesor.pick_lecture()
                            proffesor.update()
                        except TypeError as te:
                            print('input not valid')
                        except LectureError as le:
                            print(le)
                        except KeyError as ke:
                            print('input invalid')
                    case 11:
                        lectures = load_lecture()
                        display_lectures(lectures)
                        
                    case -1:
                        break
                    case _ :
                        print('input is invalid')

if __name__ == "__main__":
    main()