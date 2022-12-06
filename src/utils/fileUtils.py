import os

def fileExist(path):
    return os.path.exists(path)

def isWindows():
    return os.name == 'nt'