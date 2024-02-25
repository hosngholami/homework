from hossein_gholami_hw5.src.get_lecture import get_lecture
from hossein_gholami_hw5.src.write import write_file
from hossein_gholami_hw5.src.insert_student import insert_student
from hossein_gholami_hw5.src.load_student import load_student
from hossein_gholami_hw5.src.give_grade import give_grade
from hossein_gholami_hw5.model.student import Student
from hossein_gholami_hw5.error_message.status_grade_error import StatusGradeError
from hossein_gholami_hw5.src.insert_proffesor import insert_proffesor
from hossein_gholami_hw5.src.load_proffesor import load_proffesor
import json


def main():

    opration = {
        -1: 'exit',
        1: 'insert lecture',
        2: 'write lecture to file',
        3: 'insert student',
        4: 'write student to file',
        5: 'load student',
        6: 'give grad',
        7: 'insert proffesor',
        8: 'write proffesor to file',
        9: 'load proffesor',
        10: 'take grade with proffesor'
        
    }

    

    while True:

            for key, value in opration.items():
                print(f'{value} -> {key}')
            state = int(input('select opration: '))

            match state:
                case 1:
                    lecture =  get_lecture()
                case 2:
                    write_file(file_name='/hossein_gholami_hw5/data/book.json', file=json.dumps(lecture))
                case 3:
                    list_student = insert_student()
                case 4:
                    write_file('/hossein_gholami_hw5/data/student.json', file=json.dumps(list_student))
                case 5:
                    data = load_student()
                    for d in data:
                        print(f'student id: {d}: {data[d]}')
                case 6:
                    try:
                        student_id = input('please enter student id: ')
                        student = Student(student_id)
                        student.check_status()
                        if student.status == False:
                            raise StatusGradeError()
                        
                        student.give_grade()
                        student.update()                        
                    except StatusGradeError as sge:
                        print(sge)

                case 7:
                    proffesors = insert_proffesor()
                case 8:
                    write_file(file_name='/hossein_gholami_hw5/data/proffesor.json', file=json.dumps(proffesors))
                case 9:
                    print(load_proffesor())
                case 10:
                    pass
                    
                
                case -1:
                    break
                case _ :
                    print('input is invalid')

if __name__ == "__main__":
    main()