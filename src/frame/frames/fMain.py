
import tkinter as tk
#from tkinter import Frame
import frame.rootManager as rootManager
import utils.tkinter.tkUtils as tkUtils

import param.paramManager as paramManager

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FMAIN

from frame.frames.party.fPlay import FPlay
from frame.frames.settings.fSettings import FSettings

class FMain(IFrame):

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

        buttonPlay = super().createButton(master = frameMainButtons ,text="Jouer", cmd=lambda:rootManager.runNewFrame(FPlay(self)), fontSize=18)
        buttonPlay.pack(pady = tkUtils.ratioHeight(0.01, root), fill=tk.X)

        buttonOptions = super().createButton(master = frameMainButtons, text="Options", cmd=lambda:rootManager.runNewFrame(FSettings(self)), fontSize=18)
        buttonOptions.pack(pady = tkUtils.ratioHeight(0.01, root), fill=tk.X)


        buttonQuit = super().createButton(master = frameExit, text="Quitter", cmd=lambda:rootManager.destroyRoot(), fontSize=18)
        super().modifyButton(buttonQuit ,bg = "darkred", ab = "red")
        buttonQuit["width"] = tkUtils.ratioWidth(0.015, root)
        buttonQuit["height"] = tkUtils.ratioHeight(0.0035, root)
        buttonQuit.pack()
