def write_file(file_name: str,  data):
    with open(file_name, 'w') as file:
        file.write(data)


def read_file(file_name: str):
    with open(file_name, 'r') as file:
      return  file.readlines()
