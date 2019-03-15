def write(file, command, id):
    with open(file, 'r+') as f:
        f.write(command + ' ' + id + '\n')
        print(command + ' ' + id)