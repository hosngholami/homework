from hossein_gholami_hw5.src.insert_proffesor import insert_proffesor
from hossein_gholami_hw5.src.write import write_file
from hossein_gholami_hw5.src.load_proffesor import load_proffesor
from hossein_gholami_hw5.src.display_proffesor import display_proffesor
from hossein_gholami_hw5.model.proffesor import Proffesor
from hossein_gholami_hw5.error_message.lecture_error import LectureError
from hossein_gholami_hw5.src.display_opration import display_opration
import json
def proffesor_menu():

    oprations = {
        -1: 'exit',
        1: 'display proffesor',
        2: 'insert proffesor',
        3: 'write proffesor',
        4: 'take grade'
    }

    display_opration(oprations)
    while True:
        op = int(input('proffesor -> enter oprations: '))

        match op:
            case 1:
                proffesor = load_proffesor()
                display_proffesor(proffesor)
            case 2:
                proffesors = insert_proffesor()
            case 3:
                    try:
                        write_file(file_name='/hossein_gholami_hw5/data/proffesor.json', file=json.dumps(proffesors))
                    except UnboundLocalError as ul:
                        print('please insert proffesor')
            case 4:
                try:
                    proffesor_id = input('enter proffesor_number: ')
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

            case -1:
                break
                        