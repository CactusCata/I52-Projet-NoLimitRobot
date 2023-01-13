
import tkinter as tk
import frame.rootManager as rootManager
import utils.tkinter.tkUtils as tkUtils

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FMAIN

from frame.frames.party.fPlay import FPlay
from frame.frames.settings.fSettings import FSettings

class FMain(IFrame):
    """
    Menu qui propose à l'utilisateur de:
        - Jouer
        - Aller dans les options
        - Quitter le jeu
    """

    def __init__(self, previousFrame=None):
        super().__init__(previousFrame, HELP_FMAIN)

    def draw(self):
        root = rootManager.getRoot()
        dimensions = super().getScreenDimensions(root)

        super().createButtonHelp()

        label = super().createLabel(master = root, text=rootManager.GAME_NAME, fontSize = 50)
        label["fg"] = "lightblue"
        label.pack(side = "top", anchor = "n")

        frameMainButtons = super().createFrame(root)
        frameMainButtons.pack(pady = tkUtils.ratioHeight(0.15, root))

        frameExit = super().createFrame(root)
        frameExit.pack(side = "bottom", anchor = "e", padx = 10, pady = 10)

        # Jouer
        buttonPlay = super().createButton(master = frameMainButtons ,text="Jouer", cmd=lambda:rootManager.runNewFrame(FPlay(self)), fontSize=18)
        buttonPlay.pack(pady = tkUtils.ratioHeight(0.01, root), fill=tk.X)

        # Options
        buttonOptions = super().createButton(master = frameMainButtons, text="Options", cmd=lambda:rootManager.runNewFrame(FSettings(self)), fontSize=18)
        buttonOptions.pack(pady = tkUtils.ratioHeight(0.01, root), fill=tk.X)

        # Quitter
        buttonQuit = super().createButton(master = frameExit, text="Quitter", cmd=lambda:rootManager.destroyRoot(), fontSize=18)
        super().modifyButton(buttonQuit ,bg = "darkred", ab = "red")
        buttonQuit["width"] = tkUtils.ratioWidth(0.015, root)
        buttonQuit["height"] = tkUtils.ratioHeight(0.0035, root)
        buttonQuit.pack()
