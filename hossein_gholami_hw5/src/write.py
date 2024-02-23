import os
def write_file(file_name, file):
    print(file)
    path = os.getcwd() + file_name
    with open(path, 'w') as f:
        f.write(file)
        print('write file successfully')