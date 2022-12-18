from robot.robotManager import ROBOT_FOLDER_PATH

def get_desc_from_name(name):
    """
    Renvoie la description d'un robot
    """
    file = open(f"{ROBOT_FOLDER_PATH}{name}/instructions.rbt", "r")
    firstLine = file.readline().rstrip()
    description = firstLine[1:]
    file.close()
    return description

def get_instr_from_name(name):
    """
    Renvoie les instructions d'un robot
    """
    file = open(f"{ROBOT_FOLDER_PATH}{name}/instructions.rbt")
    fileContent = file.read()
    lines = fileContent.split('\n')[1:]
    file.close()
    return lines

def get_logo_path_from_name(name):
    """
    Renvoie le chemin du logo d'un robot
    """
    return f"{ROBOT_FOLDER_PATH}{name}/icon.png"