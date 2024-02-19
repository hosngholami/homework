def read_file(file_name):
    with open(file_name, 'r') as file:
       data =  file.readlines()
       return data
    

def write_file(file_name, data):
    with open(file_name, 'a') as file:
        file.write('\n'+data)
