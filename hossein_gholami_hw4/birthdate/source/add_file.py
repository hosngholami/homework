from source.IO import write_file
from source.search import check_user
def add_file(data, name, birthday):

    if check_user(data, name) == False:
        new_data = f'{name}-{birthday}'
        write_file('birthdays.txt', new_data)
        print(f'write {name}-{birthday} to birthdays.txt')
    else:
        print(f'{name} is exsist in birthdays.txt')
    
    