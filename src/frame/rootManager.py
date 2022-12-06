from tkinter import Tk

from frame.frames.fMain import FMain

import utils.tkUtils as tkUtils
import utils.fileUtils as fileUtils

GAME_NAME = "No Limit Robot"

root = None
currentFrame = None

def initRoot():
    """
    Initialise l'instance de la fenêtre.
    Permet une accessibilité simple depuis toute les frames.
    """
    global root

    # Crée la fenêtre
    root = Tk()

    # Dimensionne la fenêtre en fonction de l'écran de l'utilisateur
    # et bloque le dimensionnement de la fenêtre
    dimensions = tkUtils.setupRootGeometry(root, ratio=1)
    tkUtils.lockRootDimensions(root, dimensions)

    # Applique quelques propriétés à la fenêtre
    root.title(GAME_NAME)
    root.configure(background='#1E1E1E')
    if (fileUtils.isWindows()):
        root.iconbitmap('../res/img/icon.ico')
    else:
        root.iconbitmap('../res/img/icon.xbm')
    root.protocol("WM_DELETE_WINDOW", destroyRoot)

    # Lance le menu principal
    runNewFrame(FMain())

    root.mainloop()


def getRoot():
    """
    Renvoie l'instance de la fenêtre courante
    """
    return root

def destroyRoot():
    """
    Détruit la fenêtre
    """
    global root

    clearCurrentFrame()
    root.destroy()
    root = None

def clearCurrentFrame():
    """
    Supprime tous les widgets de l'écran
    A executer au préalable avant la fonction
    runNewFrame
    """
    if (currentFrame is not None):
        currentFrame.clearFrame()

def runNewFrame(frame):
    global currentFrame

    clearCurrentFrame()

    currentFrame = frame
    frame.draw()