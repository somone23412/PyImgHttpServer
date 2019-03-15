# use crontab to ensure service always online

import searchimg as si
import changefile as cf
import json
import os
from flask import Flask, request


config = {}
config['path']={'host':'10.112.126.102', 'port':'4000', 'imgPath':'/home/quyan/PycharmProjects/PyHttpServer/', 'filePath':'/home/quyan/PycharmProjects/PyHttpServer/tmp/'}
config['response']={
    'add_accept':{'status':'0', 'message':'add_accept'},
    'add_reject':{'status':'1', 'message':'add_reject_beacuse_of_id_exsists'},
    'del_accept':{'status':'0', 'message':'del_accept'},
    'del_reject':{'status':'1', 'message':'del_reject_beacuse_of_id_not_exsists'}
}

app = Flask(__name__)


@app.route('/imgadd', methods=['POST'])
def imgadd():
    recId = request.form.get('blackListPersonId')
    print('Id to add = ', recId)
    recImg = request.files['blackListPersonImg']
    print('recImg = ', recImg)
    if not si.search(config['path']['imgPath'], recId + '.jpg'):
        recImg.save(config['path']['imgPath'] + recId + '.jpg')
        cf.write(config['path']['filePath'], 'add', recId)
        print(config['response']['add_accept'])
        return json.dumps(config['response']['add_accept'])
    else:
        print(config['response']['add_reject'])
        return json.dumps(config['response']['add_reject'])


@app.route('/imgdel', methods=['DELETE'])
def imgdel():
    recId = request.form.get('deletePersonId')
    print('Id to delete = ', recId)
    if si.search(config['path']['imgPath'], recId + '.jpg'):
        cf.write(config['path']['filePath'], 'delete', recId)
        os.remove(config['path']['imgPath'] + recId + '.jpg')
        print(config['response']['del_accept'])
        return json.dumps(config['response']['del_accept'])
    else:
        print(config['response']['del_reject'])
        return json.dumps(config['response']['del_reject'])


if __name__ == '__main__':
    app.run(host=config['path']['host'], port=config['path']['port'])


