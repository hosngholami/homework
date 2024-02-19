import sys
import fileinput


# def replace(file, searchExp, replaceExp):
#    for line in fileinput.input(file, inplace=1):
#        line = line.replace(searchExp, replaceExp)
#        sys.stdout.write(line)
       

# replace('calculate.txt', 'add', 'add1')


def write(**kwargs):



    with open('calculate.txt', 'w') as calc:
        for arg in kwargs.items():
            calc.write(str(arg) + '\n')
            
        
