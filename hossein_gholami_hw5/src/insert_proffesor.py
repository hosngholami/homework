from hossein_gholami_hw5.src.load_proffesor import load_proffesor
proffesor = {}

if load_proffesor() != None:
    proffesor = load_proffesor()


def insert_proffesor():

    try:
        proffesor_id = int(input('please enter student id: '))
        name = input('plase enter name: ')
        family = input('plase enter family: ')
    except:
        pass
    else:
        proffesor[proffesor_id] = {
            'name' : name,
            'family' : family,
            'grade' : {},
            }
    
    return proffesor