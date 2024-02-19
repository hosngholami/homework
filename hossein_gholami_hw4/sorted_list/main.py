from source.user_data import get_user_data
from source.prepare_data import get_prepare_data
from source.IO import *

def main():
    data = get_user_data()
    write_file('input_file.txt', data=data)
    data = read_file('input_file.txt')
    data = get_prepare_data(str(data[0]))
    
    print(f'data: {data}')

    sort = sorted(data)
    reverse = sorted(data, reverse=True)

    text = f'{sort}\n{reverse}'
    write_file('sorted_file.txt', text)
    print(f'write sorted: {sort}')
    print(f'write reversed: {reverse}')


main()
    
