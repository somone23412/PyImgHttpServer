import json


def insert(path, id, name):
    load_dict = {}
    with open(path, 'r') as f:
        load_dict = json.load(f)
    load_dict[id] = name
    with open(path, 'w') as f:
        json.dump(load_dict, f)


def delete(path, id):
    with open(path, 'r') as load_f:
        load_dict = json.load(load_f)
    print('[ORIGINAL REC]', load_dict)
    if id in load_dict:
        name = load_dict[id]
        load_dict.pop(id)
        print('AFTER DEL REC', load_dict)
        with open(path, 'w') as dump_f:
            json.dump(load_dict, dump_f)
        return name
    else:
        return None