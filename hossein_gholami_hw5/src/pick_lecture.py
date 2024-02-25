from hossein_gholami_hw5.src.read_file import read_file 
from hossein_gholami_hw5.error_message.grade_error import GradeError
def pick_lecture():
    

    selected_list = {}
    data = read_file('/hossein_gholami_hw5/data/lecture.json')
    try:
        while True:
            code = input('enter code book: ')
            if code == -1:
                break
            if code not in selected_list.keys():
                print(data[code])
                selected_list[code] = -1
    except KeyError as ke:
        print('book is not found')
    except GradeError as ge:
        print(ge)


    return selected_list
    

  

