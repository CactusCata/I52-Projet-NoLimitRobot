
import tkinter as tk
from tkinter import Frame
import frame.rootManager as rootManager
import utils.tkinter.tkUtils as tkUtils

from frame.iFrame import IFrame, help_activated
from frame.messagesHelp import HELP_FMAIN

from frame.frames.party.fPlay import FPlay
from frame.frames.settings.fSettings import FSettings

class FMain(IFrame):

    def __init__(self):
        super().__init__()

    def draw(self):
        root = rootManager.getRoot()
        dimensions = super().getScreenDimensions(root)

        frameHelp = super().createFrame(root)
        frameHelp.pack(side = "top", anchor = "e", padx = 10, pady = 10)

        label = super().createLabel(master = root, text=rootManager.GAME_NAME, fontSize = 50)
        label["fg"] = "lightblue"
        label.pack(side = "top", anchor = "n")

        frameMainButtons = super().createFrame(root)
        frameMainButtons.pack(pady = 100)


        frameExit = super().createFrame(root)
        frameExit.pack(side = "bottom", anchor = "e", padx = 10, pady = 10)

        buttonPlay = super().createButton(master = frameMainButtons ,text="Jouer", cmd=lambda:rootManager.runNewFrame(FPlay(self)), fontSize=18)
        super().modifyButton(buttonPlay ,bg = "darkblue", ab = "blue")
        buttonPlay.pack(fill=tk.X)

        buttonOptions = super().createButton(master = frameMainButtons, text="Options", cmd=lambda:rootManager.runNewFrame(FSettings(self)), fontSize=18)
        super().modifyButton(buttonOptions ,bg = "darkviolet", ab = "violet")
        buttonOptions.pack(pady = 15, fill=tk.X)

        if help_activated == True :
            buttonHelp = super().createButtonHelp(master = frameHelp, msg=HELP_FMAIN)
            super().modifyButton(buttonHelp ,bg = "darkgreen", ab = "green")
            buttonHelp.pack()

        buttonQuit = super().createButton(master = frameExit, text="Quitter", cmd=lambda:rootManager.destroyRoot(), fontSize=18)
        super().modifyButton(buttonQuit ,bg = "darkred", ab = "red")
        buttonQuit.pack()
