from source.prepare_data import get_prepare_data
def search_user(data, name):
    data = get_prepare_data(data)
    if name in data.keys():
        return f'{name} was born in {data[name]}'
    return "user not found"


def check_user(data, name):
    data = get_prepare_data(data)
    if name in data.keys():
        return True
    return False