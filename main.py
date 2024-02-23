from hossein_gholami_hw5.src.get_lecture import get_lecture
from hossein_gholami_hw5.src.write import write_file
import json


def main():

    opration = {
        -1: 'exit',
        1: 'insert lecture',
        2: 'write lecture',
        
    }

    

    while True:
        print(opration)
        state = int(input('select opration: '))

        match state:
            case 1:
                 lecture =  get_lecture()
            case 2:
                 write_file(file_name='/hossein_gholami_hw5/data/book.json', file=json.dumps(lecture))
            case -1:
                break
            case _ :
                print('input is invalid')
            

       

if __name__ == "__main__":
    main()