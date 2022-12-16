import utils.fileUtils as fileUtils
import os
import shutil


ROBOT_EXTENSION_NAME = "rbt"
ROBOT_FOLDER_PATH = "../config/robots/"

robotnames = []

def loadRobotsNames():
    """
    Récupère tous les noms de robots utilisés depuis le dossier config/robots
    """
    global robotnames
    robotnames = fileUtils.getAllFileInDirectory(ROBOT_FOLDER_PATH)
    print(f"robotNames : {robotnames}")

def getLoadedRobots():
    """
    Renvoie la liste de tous les noms de dossier présents dans
    le dossier config/maps
    """
    return robotnames

def createNewRobot(name, desc = "", nbinstr = 6, logoPath=None):
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
    createRobotProperties(realname, realdesc)
    createRobotLogo(realname, logoPath)
    createRobotInstructions(realname, nbinstr) #Mettre des commandes de bases du style 6 x déplacements

def createRobotDirectory(name):
    """
    Créée un répertoire du nom du robot mit en paramètre
    """
    os.mkdir(f"../config/robots/{name}") #chemin relatif depuis le main.py

def uglynametorealname(name):
    """
    Transforme e la chaîne de caractère extraite depuis la boite textuelle
    en une chaîne claire qui est retournée, sans les caractères qui n'ont pas lieu d'être, notamment
    le '\n'

    """
    realname = ""
    for c in name:
        if c == '\n':
            return realname
        else:
            realname += c

def createRobotProperties(name, desc=""):
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

def createRobotLogo(name, logoPath):
    if (not os.path.exists(logoPath)):
        logoPath = "res/img/robot/default_robot.png"

    shutil.copyfile(logoPath, f"{ROBOT_FOLDER_PATH}{name}/icon.png")
