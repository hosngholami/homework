def get_prepare_data(data):
    user_data = {}
    for item in data:
        item = str(item)
        item = item.split('-')
        item[1] = item[1].replace('\n' ,'')
        if item[0] not in  user_data.keys():
            user_data[item[0]] = item[1]
    return user_data