from hossein_gholami_hw5.error_message.str_input_error import StrInputError
from hossein_gholami_hw5.error_message.exist_error import ExistError
from hossein_gholami_hw5.src.read_file import read_file
def insert_lecture():
    books = read_file('/hossein_gholami_hw5/data/lecture.json')
    print('enter -1 for exit')
    while True:
        try:
            code = input('enter code lecture: ')
            if code == "-1":
                break
            
            if code in books.keys():
                raise ExistError(f'{code} is exist')
            
            title = input('enter book name: ')

            if type(title) == int:
                raise StrInputError('title is not valid')
       
        except ValueError as ve:
            print('code is not valid')
        except StrInputError as si:
            print(si)
        except ExistError as ee:
            print(ee)
        else:
            books[code] = title

    return books
        
            