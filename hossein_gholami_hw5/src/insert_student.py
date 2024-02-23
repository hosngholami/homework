from hossein_gholami_hw5.src.load_student import load_student
students = load_student()


def insert_student():



    student_id = int(input('please enter student id: '))
    name = input('plase enter name: ')
    family = input('plase enter family: ')
    books = input('enter list book sperate with space: ')

    students[student_id] = {
        'name' : name,
        'family' : family,
        'books'  : books

    }

    return students
