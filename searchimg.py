import os

def search(path, name):
    for root, dirs, files in os.walk(path):
        if name in dirs or name in files:
            root = str(root)
            dirs = str(dirs)
            return os.path.join(root, dirs)
    return False