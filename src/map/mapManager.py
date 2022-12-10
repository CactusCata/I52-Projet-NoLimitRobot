import utils.fileUtils as fileUtils
import json
from map.map import Map

MAP_EXTENSION_NAME = "dat"
MAP_FOLDER_PATH = "../config/maps/"

MAP_LINE_AMOUNT = 20
MAP_COL_AMOUNT = 30
MAP_MAX_ROCK_PERCENTAGE = 20
MAP_MAX_ROCK_AMOUNT = int((MAP_MAX_ROCK_PERCENTAGE / 100) * MAP_LINE_AMOUNT * MAP_COL_AMOUNT)

mapNames = []

def loadMapNames():
    """
    Charge le nom des maps dans le dossier config/maps/
    """
    global mapNames
    mapNamesAndExtension = fileUtils.getAllFileInDirectory(MAP_FOLDER_PATH)
    mapNames = []

    for mapNameAndExtension in mapNamesAndExtension:
        mapNames.append(mapNameAndExtension.split(".")[0])

def getLoadedMaps():
    """
    Renvoie la liste de tous les noms de dossier présents dans
    le dossier config/maps
    """
    return mapNames

def createNewMap(mapName):
    """
    Ajoute dans la liste des maps la nouvelle map
    et créé le fichier de la map dans le dossier config/maps
    """
    mapNames.append(mapName)
    createMapFile(mapName)

def createMapFile(mapName):
    """
    Crée le fichier de la map avec une
    matrice de terrain (vide).
    """
    file = open(f"{MAP_FOLDER_PATH}{mapName}.{MAP_EXTENSION_NAME}", "w")

    map = [[0] * 30] * 20
    file.write(json.dumps(map))
    file.close()

def loadMapFileContent(mapName):
    """
    Renvoie le contenu du fichier de la map
    """
    file = open(f"{MAP_FOLDER_PATH}{mapName}.{MAP_EXTENSION_NAME}", "r")

    mapFileContent = json.load(file)
    file.close()
    return Map(mapFileContent)

def saveMap(mapName, map):
    """
    Sauvegarde dans un fichier la map
    """
    file = open(f"{MAP_FOLDER_PATH}{mapName}.{MAP_EXTENSION_NAME}", "w")

    mapMatrix = map.getMatrix()
    file.write(json.dumps(mapMatrix))
    file.close()

def deleteMap(mapName):
    """
    Supprime la map de la liste des maps chargées
    et supprime son fichier associé
    """
    mapNames.remove(mapName)
    fileUtils.deleteFile(f"{MAP_FOLDER_PATH}{mapName}.{MAP_EXTENSION_NAME}")