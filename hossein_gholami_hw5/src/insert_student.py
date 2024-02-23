from hossein_gholami_hw5.src.load_student import load_student
students = load_student()


def insert_student():

    try:
        student_id = int(input('please enter student id: '))
        name = input('plase enter name: ')
        family = input('plase enter family: ')
    except:
        pass
    else:
        students[student_id] = {
            'name' : name,
            'family' : family,
            'grade' : {},
            'status' : True
            }
    
    return students
