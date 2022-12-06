import os

def fileExist(path):
    return os.path.exists(path)

def isWindows():
    return os.name == 'nt'

def getAllFileInDirectory(path):
    return os.listdir(path)

def deleteFile(file):
    os.remove(file)