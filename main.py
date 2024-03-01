from hossein_gholami_hw5.src.lecture_menu import lecture_menu
from hossein_gholami_hw5.src.student_menu import student_menu
from hossein_gholami_hw5.src.proffesor_menu import proffesor_menu
from hossein_gholami_hw5.src.display_opration import display_opration




def main():

    oprations = {
        -1: 'exit',
         1: 'lecture',
         2: 'student',
         3: 'proffesor'
        
    }
    print('#### Help ######')
    print('enter -1 for save and exit on opration')
    print('if you can saved file, you should write to file')

    print('-------------------------')
    print('#### Condition ##### ')
    print("if student avg lower 12, can't take a lecture ")
    print("proffesor can't take lecture biger 3 ")

    print('---------------------------------')

    

    print('---------------------------')


    display_opration(oprations)
    while True:
            try:
                op = int(input('main - select opration: '))
            except ValueError as ve:
                print('input is invalid')

            else:
                match op:
                    case 1:
                        lecture_menu()
                    case 2:
                        student_menu()
                    case 3:
                        proffesor_menu()
                    case -1:
                        break
                    case _ :
                        print('input is invalid')

if __name__ == "__main__":
    main()