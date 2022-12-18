import utils.fileUtils as fileUtils
import os
import shutil


ROBOT_EXTENSION_NAME = "rbt"
ROBOT_FOLDER_PATH = "../config/robots/"
ROBOT_MIN_INSTRUCTION_AMOUNT = 6
ROBOT_MAX_INSTRUCTION_AMOUNT = 20
ROBOT_DEFAULT_INSTRUCTIONS = ["FT", "AL", "MI", "AL", "MI", "AL"]
ROBOT_DEFAULT_LOGO_PATH = "../res/img/robot/default_robot.png"

robotnames = []

def loadRobotsNames():
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

def createNewRobot(name, description="", instructions=[], logoPath=None):
    """
    Créée un nouveau robot en ajoutant son nom dans la liste des noms puis
    créée un répertoire du nom du robot
    """
    if name not in robotnames:
        createRobotDirectory(name)
        createRobotDescAndInstructs(name, description, instructions)
        createRobotLogo(name, logoPath)
        robotnames.append(name)

def updateRobot(name, description, instructions):
    """
    Met à jour la description et les instructions d'un robot
    """
    createRobotDescAndInstructs(name, description, instructions)

def createRobotDirectory(name):
    """
    Créée un répertoire du nom du robot mit en paramètre
    """
    os.mkdir(f"{ROBOT_FOLDER_PATH}{name}") #chemin relatif depuis le main.py

def createRobotDescAndInstructs(name, description, instructions):
    """
    Créée le fichier instructions.rbt dans le dossier du robot avec comme attributs
    la description et les instructions
    """
    file = open(f"{ROBOT_FOLDER_PATH}{name}/instructions.{ROBOT_EXTENSION_NAME}", "w")
    file.write(";" + description + "\n")

    if len(instructions) < ROBOT_MIN_INSTRUCTION_AMOUNT:
        instructions = ROBOT_DEFAULT_INSTRUCTIONS

    if len(instructions) > 0:
        for i in range(len(instructions) - 1):
            file.write(f"{instructions[i]}\n")
        file.write(f"{instructions[len(instructions) - 1]}")

    file.close()

def createRobotLogo(name, logoPath):
    """
    Copie du fichier logo dans le repertoire de configuration du robot
    Si le logo n'est pas correct, met un robot par défaut
    """
    if (logoPath == None) or (not os.path.exists(logoPath)):
        logoPath = ROBOT_DEFAULT_LOGO_PATH

    shutil.copyfile(logoPath, f"{ROBOT_FOLDER_PATH}{name}/icon.png")

def deleteRobot(name):
    """
    Supprime les fichiers associés à un robot
    """
    if (name not in robotnames):
        return

    os.remove(f"{ROBOT_FOLDER_PATH}{name}/icon.png")
    os.remove(f"{ROBOT_FOLDER_PATH}{name}/instructions.{ROBOT_EXTENSION_NAME}")
    os.rmdir(f"{ROBOT_FOLDER_PATH}{name}")
    robotnames.remove(name)