import json


def json_read(file_name, encode):
    try:
        file = open(file_name, encoding=encode)
        list_of_dict = json.load(file)
        keys_list = (list(list_of_dict[0].keys()))
        list_of_list = list()
        for i in range(len(list_of_dict)):
            list_of_list.append([])
            for key in list_of_dict[i].keys():
                list_of_list[i].append(list_of_dict[i][key])
        list_of_list.insert(0, keys_list)
        return list_of_list
    except json.decoder.JSONDecodeError:
        return print("Формат не валиден")
