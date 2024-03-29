from tkinter import Tk, PhotoImage

from frame.frames.fMain import FMain

import param.paramManager as paramManager
import image.imageManager as imageManager

"""
Fichier qui a pour objectif de travailler avec la classe mère
des frames IFrame.
"""

GAME_NAME = "No Limit Robot"

root = None
currentFrame = None

mainFrame = None

def initRoot():
    """
    Initialise l'instance de la fenêtre.
    Permet une accessibilité simple depuis toute les frames.
    """
    global root, mainFrame

    # Crée la fenêtre
    root = Tk()
    paramManager.PARAM.applyFullScreenState(root)

    imageManager.loadImagesTk()

    # Applique quelques propriétés à la fenêtre
    root.title(GAME_NAME)
    root.configure(background='#1E1E1E')

    icon = PhotoImage(file='../res/img/icon.png')
    root.iconphoto(False, icon)
    root.protocol("WM_DELETE_WINDOW", destroyRoot)

    # Lance le menu principal
    mainFrame = FMain()
    runNewFrame(mainFrame)

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
    """
    Déssine une nouvelle frame
    """
    global currentFrame

    clearCurrentFrame()

    currentFrame = frame
    frame.draw()
