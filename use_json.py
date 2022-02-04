import json


def read_json(name):
    with open(f'{name}.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def write_json(name, data):
    with open(f'{name}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)
