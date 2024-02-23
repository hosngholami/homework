from hossein_gholami_hw5.src.get_lecture import get_lecture
from hossein_gholami_hw5.src.write import write_file
from hossein_gholami_hw5.src.insert_student import insert_student
from hossein_gholami_hw5.src.load_student import load_student
import json


def main():

    opration = {
        -1: 'exit',
        1: 'insert lecture',
        2: 'write lecture',
        3: 'insert student',
        4: 'write student',
        5: 'load student'
        
    }

    

    while True:
        print(opration)
        state = int(input('select opration: '))

        match state:
            case 1:
                 lecture =  get_lecture()
            case 2:
                 write_file(file_name='/hossein_gholami_hw5/data/book.json', file=json.dumps(lecture))
            case 3:
                 list_student = insert_student()
            case 4:
                 write_file('/hossein_gholami_hw5/data/student.json',file=json.dumps(list_student))
            case 5:
                data = load_student()
                for d in data:
                    print(f'student id: {d}: {data[d]}')
            
            case -1:
                break
            case _ :
                print('input is invalid')
            

       

if __name__ == "__main__":
    main()