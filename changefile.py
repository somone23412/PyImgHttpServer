import os


def write(path, command, id):
    for file in os.listdir(path):
        os.rename(os.path.join(path, file), os.path.join(path, command + "___" + id))
        print('[COMMAND] ' + command + '___' + id)



