import os


def start(other_app_conf):
    for i in range(other_app_conf['appGPUNum']):
        cmd = other_app_conf['path']['appPath'] + other_app_conf['appName'] + ' -' + other_app_conf['appWindow']['windowless'] + ' -gpu ' + str(i) + ' >/dev/null' + ' &';
        os.system(cmd)


def shutdown(appName):
    r = os.popen('pgrep ' + appName)
    pgrep_res = r.read()
    r.close()
    pids = pgrep_res.split("\n")
    for pid in pids:
        if pid != '':
            print('[KILL] ' + appName + ' pid=', pid)
            os.system('kill ' + pid)