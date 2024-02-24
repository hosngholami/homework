from hossein_gholami_hw5.src.read_file import read_file 
from hossein_gholami_hw5.error_message.grade_error import GradeError
def give_grade():
    

    selected_list = {}
    data = read_file('/hossein_gholami_hw5/data/book.json')
    try:
        while True:
            code = input('enter code book: ')
            if code == -1:
                break
            if code not in selected_list.keys():
                print(data[code])
                grade = input('please enter grade: ')
                if int(grade) > 20 or int(grade) < 0:
                    raise GradeError(message='invalid grade', grade=grade)
                selected_list[code] = grade
    except KeyError as ke:
        print('book is not found')
    except GradeError as ge:
        print(ge)


    return selected_list
    

  

