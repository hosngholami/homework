import json
import os 
def read_file(file_name) -> dict:
    path = os.getcwd() + file_name
    with open(path, 'r') as f:
        data = json.load(f)
        return data
    