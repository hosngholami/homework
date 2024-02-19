from source.IO import read_file
from source.search import search_user
from source.add_file import add_file 
def main():
    
    data = read_file('birthdays.txt')
    
    
    print('chose an option: ')
    print('1- search a name')
    print('2- add a new data')
    status = int(input('enter 1 or 2: '))
    match status:
        case 1:
            name = input('search a name find out his or her birthday: ')
            print(search_user(data, name))
        case 2:
            name = input('enter new name: ')
            birthday = input('enter a birthday: ')
            add_file(data, name, birthday)



main()

