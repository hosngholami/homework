from hossein_gholami_hw5.src.insert_lecture import insert_lecture   
from hossein_gholami_hw5.src.write import write_file
from hossein_gholami_hw5.src.display_lecture import display_lectures
from hossein_gholami_hw5.src.load_lecture import load_lecture
from hossein_gholami_hw5.src.display_opration import display_opration
import json

def lecture_menu():

    oprations = {
        -1: 'exit',
        1: 'display lecture',
        2: 'insert lecture',
        3: 'write lectrue'
    }

    display_opration(oprations)
    while True:
        try:
            op = int(input('lecture menu - enter operation:'))
            match op:
                case 1:
                    get_lecture = load_lecture()
                    display_lectures(get_lecture)
                case 2:
                    lecture = insert_lecture()
                case 3:
                    write_file(file_name='/hossein_gholami_hw5/data/book.json', file=json.dumps(lecture))

                case -1:
                    break
        except UnboundLocalError as ule:
            print('firt,you sholud insert lecture')
        