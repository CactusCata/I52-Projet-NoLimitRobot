import utils.fileUtils as fileUtils
import json

MAP_EXTENSION_NAME = "rbt"
MAP_FOLDER_PATH = "../config/robots/"

robotnames = []

def LoadRobotsNames():
    """
    Récupère tous les noms de robots utilisés depuis le dossier config/robots
    """
    global robotnames
    robotNames = fileUtils.getAllFileInDirectory(MAP_FOLDER_PATH)

def getLoadedRobots():
    """
    Renvoie la liste de tous les noms de dossier présents dans
    le dossier config/maps
    """
    return robotnames

def createNewRobot(name, desc = "", pathlogo = "", nbsteps = 5):
    """
    Créée un nouveau robot en ajoutant son nom dans la liste des noms puis
    créée un répertoire du nom du robot
    """
    robotNames.append()
    createRobotDirectory()
    createRobotProperties(name, desc)
    createRobotInstructions() #Mettre des commandes de bases du style 6 x déplacements
    createRobotLogo()

def createRobotDirectory(name):
    """
    Créée un répertoire du nom du robot mit en paramètre
    """
    return 1

def createRobotProperties(name, desc, nbsteps):
    """
    Créée le fichier properties.rbt dans le dossier du robot avec comme attributs
    la description qu'elle soit vierge ou non, ainsi que le nombre de pas du robot
    compris entre 5 et 20 pas
    """
    return 1

def createRobotInstructions(nbinstr=6):
    """
    Créée le fichier instructions.rbt dans le dossier du robot
    """
    file = open(f"{MAP_FOLDER_PATH}{name}/","w")
    return 1

def createRobotLogo(pathlogo):
    """
    Créée le fichier logo.png en copiant un png choisit par l'utilisateur, sinon
    un png par défaut
    """
    return 1
