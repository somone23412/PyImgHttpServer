import os


def write(path, command, id, name):
    for file in os.listdir(path):
        os.rename(os.path.join(path, file), os.path.join(path, command + "___" + id + '___' + name))
        print('[COMMAND] ' + command + '___' + id + '___' + name)



