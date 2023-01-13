import json

from param.param import Param

PARAM_FILE_PATH_NAME_EXTENSION = "../config/param.dat"

PARAM = None

def loadParam():
    """
    Charge les paramètres
    """
    global PARAM

    file = open(f"{PARAM_FILE_PATH_NAME_EXTENSION}", "r")
    paramFileContent = json.load(file)
    file.close()
    PARAM = Param(fullScreenState=paramFileContent["fullScreenState"], needHelpState=paramFileContent["needHelpState"])

def saveParam():
    """
    Sauvegarde l'état actuel des paramètres
    """

    if (PARAM.optionsHasChanged):
        file = open(f"{PARAM_FILE_PATH_NAME_EXTENSION}", "w")
        paramSerialized = PARAM.serializeParam()
        file.write(json.dumps(paramSerialized))
        file.close()