import utils.fileUtils as fileUtils
from PIL import Image, ImageTk

MAP_BLOC_DIMENSIONS = (20, 20)

MAP_EXTENSION_NAME = "dat"
MAP_FOLDER_PATH = "../config/maps/"

IMG_MAP_ROCK = None
IMG_MAP_ROCK_TK = None

IMG_MAP_MINE = None
IMG_MAP_MINE_TK = None

IMG_MAP_AIR = None
IMG_MAP_AIR_TK = None

def loadImages():
    global IMG_MAP_ROCK, IMG_MAP_AIR, IMG_MAP_MINE

    IMG_MAP_ROCK = loadImage("../res/img/map/rock.png", MAP_BLOC_DIMENSIONS)
    IMG_MAP_AIR = loadImage("../res/img/map/air.png", MAP_BLOC_DIMENSIONS)
    IMG_MAP_MINE = loadImage("../res/img/map/mine.png", MAP_BLOC_DIMENSIONS)

def loadImage(path, dimensions):
    if (not fileUtils.fileExist(path)):
        print(f"Le fichier \"{path}\" n'existe pas")
        return None

    img = Image.open(path)
    img = img.resize(dimensions)
    return img

def loadImagesTk():
    global IMG_MAP_ROCK_TK, IMG_MAP_AIR_TK, IMG_MAP_MINE_TK

    IMG_MAP_ROCK_TK = loadImageTk(IMG_MAP_ROCK)
    IMG_MAP_AIR_TK = loadImageTk(IMG_MAP_AIR)
    IMG_MAP_MINE_TK = loadImageTk(IMG_MAP_MINE)

def loadImageTk(img):
    return ImageTk.PhotoImage(img)