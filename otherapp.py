import os
# Shielding caffe output
os.environ['GLOG_minloglevel'] = '2'

other_app_conf = {}
other_app_conf['appName'] = 'ubuntu_qtlx003'
other_app_conf['appGPUNum'] = 2
other_app_conf['path'] = {
    # 'appPath':'/home/quyan/QtProjects/build-ubuntu_qtlx003-Desktop_Qt_5_9_3_GCC_64bit-Release/',
    'appPath':'./',
    'getip':'http://10.106.128.94:9123',
    'postip':'http://10.106.128.94:9123'
}


def start(windowless):
        for i in range(other_app_conf['appGPUNum']):
            cmd = other_app_conf['path']['appPath'] + other_app_conf['appName'] \
                  + ' -getip ' + other_app_conf['path']['getip'] + ' -postip ' + other_app_conf['path']['postip']
            if windowless:
                cmd = cmd + ' -windowless' + ' -gpu ' + str(i) + ' &'
            else:
                cmd = cmd + ' -window' + ' &'
            os.system(cmd)


def shutdown():
    r = os.popen('pgrep ' + other_app_conf['appName'])
    pgrep_res = r.read()
    r.close()
    pids = pgrep_res.split("\n")
    for pid in pids:
        if pid != '':
            print('[KILL] ' + other_app_conf['appName'] + ' pid=', pid)
            os.system('kill ' + pid)
