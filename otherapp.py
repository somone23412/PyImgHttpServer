import os
# Shielding caffe output
os.environ['GLOG_minloglevel'] = '2'

other_app_conf = {}
other_app_conf['appName'] = 'ubuntu_qtlx003'
other_app_conf['appWindow'] = {'windowless': 'windowless', 'window': ''}
other_app_conf['appGPUNum'] = 2
other_app_conf['path'] = {'appPath': '/home/quyan/QtProjects/build-ubuntu_qtlx003-Desktop_Qt_5_9_3_GCC_64bit-Debug/'}


def start():
    for i in range(other_app_conf['appGPUNum']):
        cmd = other_app_conf['path']['appPath'] + other_app_conf['appName'] + ' -' + other_app_conf['appWindow']['windowless'] + ' -gpu ' + str(i) + ' >/dev/null' + ' &';
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