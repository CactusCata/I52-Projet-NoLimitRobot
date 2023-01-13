import os

def fileExist(path):
    """
    Renvoie True si le fichier existe
    Sinon renvoie False
    """
    return os.path.exists(path)

def isWindows():
    """
    Renvoie True si l'utilisateur est sur windows
    Sinon renvoie False
    """
    return os.name == 'nt'

def getAllFileInDirectory(path):
    """
    Renvoie la liste des fichiers dans le dossier demandé
    """
    return os.listdir(path)

def deleteFile(file):
    """
    Supprime un fichier
    """
    os.remove(file)