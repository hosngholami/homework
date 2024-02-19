from source.add import add
from source.sub import sub
from source.multiplication import multiplication
from source.division import division
from source.IO import write




def main():

    list_number = input('enter number seprate with space: ')

    list_number = list_number.split(' ')
    list_number = list(map(int, list_number))

    add_number = add(list_number)    
    sub_number = sub(list_number)
    multiplication_number = multiplication(list_number)
    division_number = division(list_number)
    print('write result in calculate.txt ... ')
    write(add=add_number, 
          sub=sub_number,
          multiplication=multiplication_number, 
          division=division_number)

    return (f'add: {add_number}', f'sub: {sub_number}', f'multiplication: {multiplication_number}', f'division: {division_number}')

print(main())