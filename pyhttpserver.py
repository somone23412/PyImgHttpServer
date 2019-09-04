# use crontab to ensure service always online
import os
import sys
import searchimg as si
import changefile as cf
import otherapp as oa
import namelist as nl
import getip as gi
import json
import filetype
from flask import Flask, request
import redis


app = Flask(__name__)


@app.route('/imgadd', methods=['POST'])
def imgadd():
    print('/---------------------PHASE:ADD-------------------------------------------/')
    print ('[REQUEST.FORM]', request.form)
    print ('[REQUEST.FILES]', request.files)

    recId = request.form.get('blackListPersonId')
    recName = request.form.get('blackListPersonName')
    recImg = request.files['blackListPersonImg']
    print(recImg)
    newId = recId
    filename = config['path']['imgPath'] + newId + '.jpg'
    if not si.search(config['path']['imgPath'], newId + '.jpg'):
        recImg.save(filename)
        #file type
        kind = filetype.guess(filename)
        if (not kind is None) and (kind.extension == 'jpg'):
            nl.insert(config['path']['record'], config['path']['imgPath'], recId, recName, redis_client)
            cf.write(config['path']['filePath'], 'add', newId)
            print('[RESPONSE]', config['response']['add_accept'])
            return json.dumps(config['response']['add_accept'])
        else:
            os.remove(filename)
            print('[RESPONSE]', config['response']['imgtype_reject'])
            return json.dumps(config['response']['imgtype_reject'])

    else:
        print('[RESPONSE]', config['response']['add_reject'])
        return json.dumps(config['response']['add_reject'])



@app.route('/imgdel', methods=['DELETE'])
def imgdel():
    print('/---------------------PHASE:DEL-------------------------------------------/')
    print ("[REQUEST.FORM]", request.form)

    recId = request.form.get('deletePersonId')
    recName = nl.delete(config['path']['record'], recId, redis_client)
    if recName is None:
        print('[RESPONSE]', config['response']['del_reject'])
        return json.dumps(config['response']['del_reject'])
    newId = recId
    filename = config['path']['imgPath'] + newId + '.jpg'
    if si.search(config['path']['imgPath'], newId + '.jpg'):
        cf.write(config['path']['filePath'], 'delete', newId)
        os.remove(filename)
        print('[RESPONSE]', config['response']['del_accept'])
        return json.dumps(config['response']['del_accept'])
    else:
        print('[RESPONSE]', config['response']['del_reject'])
        return json.dumps(config['response']['del_reject'])


if __name__ == '__main__':

    config = {}
    config['port'] = '4000'
    config['path'] = {
        'imgPath': './imgrc/',
        'filePath': './tmp/',
        'record':'./record.json'
    }
    config['response'] = {
        'add_accept': {'status': '0', 'message': 'add_accept'},
        'add_reject': {'status': '1', 'message': 'add_reject_beacuse_of_id_exsists'},
        'imgtype_reject': {'status': '1', 'message': 'add_reject_beacuse_of_not_a_jpg_img'},
        'del_accept': {'status': '0', 'message': 'del_accept'},
        'del_reject': {'status': '1', 'message': 'del_reject_beacuse_of_id_not_exsists'}
    }
    
    

    currentpath = os.getcwd()
    # oa.start(windowless=True)
    # os.system('python3 protectprocess.py --process_num 2 &')
    # host = gi.get_host_ip()
    host = '172.27.218.163'
    redis_client = redis.Redis(host='192.168.2.217', password='redistrans', port=8379)
    app.run(host=host, port=config['port'])
    # oa.shutdown()




