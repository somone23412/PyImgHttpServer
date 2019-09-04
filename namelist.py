import json


def insert(path, img_path, id, name, redis_client):
    target_id = id.split('_')[0]
    type = id.split('_')[-1]
    if type == '0':
        type = 'white'
    elif type == '2':
        type = 'red'
    else:
        type = 'black'
    load_dict = {}
    with open(path, 'r') as f:
        load_dict = json.load(f)
    load_dict[type][target_id] = name
    # json_dcit = json.dumps(load_dict)
    with open(path, 'w') as f:
        json.dump(load_dict, f)
    img_file = open(img_path + id + '.jpg','rb')
    img_data = img_file.read()
    img_size = img_file.tell()
    img_file.close()
    # img_data = bytearray(img_data)
    redis_client.set('re_templ_' + target_id, img_data)
    redis_client.set('re_templ_list', json.dumps(load_dict))


def delete(path, id, redis_client):
    target_id = id.split('_')[0]
    with open(path, 'r') as load_f:
        load_dict = json.load(load_f)
    print('[ORIGINAL REC]', load_dict)
    type = None
    if target_id in load_dict['white']:
        type = 'white'
    elif target_id in load_dict['red']:
        type = 'red'
    elif target_id in load_dict['black']:
        type = 'black'
    
    if type is not None:
        name = load_dict[type][target_id]
        load_dict[type].pop(target_id)
        print('AFTER DEL REC', load_dict)
        with open(path, 'w') as dump_f:
            json.dump(load_dict, dump_f)
        redis_client.delete('re_templ_' + target_id)
        redis_client.set('re_templ_list', json.dumps(load_dict))
        return name
    else:
        return None