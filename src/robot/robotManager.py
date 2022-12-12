import utils.fileUtils as fileUtils
import json
import os

ROBOT_EXTENSION_NAME = "rbt"
ROBOT_FOLDER_PATH = "../config/robots/"

robotnames = []

def LoadRobotsNames():
    """
    Récupère tous les noms de robots utilisés depuis le dossier config/robots
    """
    global robotnames
    robotnames = fileUtils.getAllFileInDirectory(ROBOT_FOLDER_PATH)

def getLoadedRobots():
    """
    Renvoie la liste de tous les noms de dossier présents dans
    le dossier config/maps
    """
    return robotnames

def createNewRobot(name, desc = "", nbinstr = 6):
    """
    Créée un nouveau robot en ajoutant son nom dans la liste des noms puis
    créée un répertoire du nom du robot
    """
    if name in robotnames:
        return False
    else:
        robotnames.append(name)
    realname = uglynametorealname(name)
    realdesc = uglynametorealname(desc)
    createRobotDirectory(realname)
    createRobotProperties(realname, dir, realdesc)
    createRobotInstructions(realname, nbinstr) #Mettre des commandes de bases du style 6 x déplacements

def createRobotDirectory(name):
    """
    Créée un répertoire du nom du robot mit en paramètre
    """
    os.mkdir(f"../config/robots/{name}") #chemin relatif depuis le main.py

def uglynametorealname(name):
    realname = ""
    for c in name:
        if c == '\n':
            return realname
        else:
            realname += c

def createRobotProperties(name, dir, desc=""):
    """
    Créée le fichier properties.rbt dans le dossier du robot avec comme attributs
    la description qu'elle soit vierge ou non
    """
    file = open(f"{ROBOT_FOLDER_PATH}{name}/properties.rbt", "w")
    file.write(desc)
    file.close()


def createRobotInstructions(name, nbinstr):
    """
    Créée le fichier instructions.rbt dans le dossier du robot
    """
    file = open(f"../config/robots/{name}/instructions.rbt", "w")
    mininst = f";Robot du nom de {name}\n!FT\nAL\nMI\nAL\nMI\nAL" #Information puis urgence puis n les instructions
    file.write(mininst)
    file.close()
