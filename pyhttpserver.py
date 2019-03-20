# use crontab to ensure service always online
import os
import searchimg as si
import changefile as cf
import otherapp as oa
import json
import filetype
from flask import Flask, request


app = Flask(__name__)


@app.route('/imgadd', methods=['POST'])
def imgadd():
    print('/---------------------PHASE:ADD-------------------------------------------/')
    print ('[REQUEST.FORM]', request.form)
    print ('[REQUEST.FILES]', request.files)

    recId = request.form.get('blackListPersonId')
    recName = request.form.get('blackListPersonName')
    recImg = request.files['blackListPersonImg']
    filename = config['path']['imgPath'] + recId + '.jpg'
    if not si.search(config['path']['imgPath'], recId + '.jpg'):
        recImg.save(filename)
        #file type
        kind = filetype.guess(filename)
        if (not kind is None) and (kind.extension == 'jpg'):
            cf.write(config['path']['filePath'], 'add', recId, recName)
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
    filename = config['path']['imgPath'] + recId + '.jpg'
    if si.search(config['path']['imgPath'], recId + '.jpg'):
        cf.write(config['path']['filePath'], 'delete', recId, name="anyname")
        os.remove(filename)
        print('[RESPONSE]', config['response']['del_accept'])
        return json.dumps(config['response']['del_accept'])
    else:
        print('[RESPONSE]', config['response']['del_reject'])
        return json.dumps(config['response']['del_reject'])


if __name__ == '__main__':

    config = {}
    config['http'] = {'host': '10.112.126.102', 'port': '4000'}
    config['path'] = {
        'imgPath': '/home/quyan/PycharmProjects/PyHttpServer/',
        'filePath': '/home/quyan/PycharmProjects/PyHttpServer/tmp/',
    }
    config['response'] = {
        'add_accept': {'status': '0', 'message': 'add_accept'},
        'add_reject': {'status': '1', 'message': 'add_reject_beacuse_of_id_exsists'},
        'imgtype_reject': {'status': '1', 'message': 'add_reject_beacuse_of_not_a_jpg_img'},
        'del_accept': {'status': '0', 'message': 'del_accept'},
        'del_reject': {'status': '1', 'message': 'del_reject_beacuse_of_id_not_exsists'}
    }

    oa.start()
    app.run(host=config['http']['host'], port=config['http']['port'])
    oa.shutdown()




