import os
# Shielding caffe output
os.environ['GLOG_minloglevel'] = '2'

other_app_conf = {}
other_app_conf['appName'] = 'ubuntu_qtlx003'
other_app_conf['appGPUNum'] = 2
other_app_conf['path'] = {
    'appPath':'./',
}
other_app_conf['video_nums'] = 2
# (configId, gpuId)
config = {}
config['0'] = '0'
config['1'] = '0'
config['2'] = '1'
config['3'] = '1'

def start(windowless):
        for key in config.keys():
            cmd = other_app_conf['path']['appPath'] + other_app_conf['appName']
            if windowless:
                cmd = cmd + ' -windowless' + ' -gpu ' + config[key] + ' -config ' + key + ' &'
            else:
                cmd = cmd + ' -config ' + key + ' &'
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
