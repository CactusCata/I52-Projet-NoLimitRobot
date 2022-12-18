from robot.robotManager import ROBOT_FOLDER_PATH

def get_desc_from_name(name):
    """
    Retourne la description d'un robot dans le fichier instruction.rbt affilié à
    celui-ci. La donnée retournée est une chaîne de caractère.
    """
    file = open(f"{ROBOT_FOLDER_PATH}{name}/instructions.rbt", "r")
    firstLine = file.readline().rstrip()
    description = firstLine[1:]
    file.close()
    return description

def get_instr_from_name(name):
    """
    Retourne une liste composée de l'instruction d'urgence en position 0, et de
    n instructions en position de 1 à n-1 inclus. Ces instructions sont extraites
    depuis le ficher instructions.rbt du robot affilié.
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