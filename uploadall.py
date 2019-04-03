import os
import time
import filetype
import changefile as cf

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)
        print(dirs)
        print(files)
        return files


if __name__ == '__main__':
    files = file_name('./upload/')

    for file in files:
        filepath = './upload/' + file
        #print(filepath)
        kind = filetype.guess(filepath)
        print(kind)
        if (not kind is None) and (kind.extension == 'jpg'):
            # os.rename(os.path.join('./upload/', file), os.path.join('./upload/', file.split('.')[0] + '_0.jpg'))
            cf.write('./tmp/', 'add', file.split('.')[0])
            time.sleep(0.05)
