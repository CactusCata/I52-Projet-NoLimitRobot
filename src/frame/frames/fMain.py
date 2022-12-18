from tkinter import Frame, BOTH, font

import frame.rootManager as rootManager
import utils.tkinter.tkUtils as tkUtils

from frame.iFrame import IFrame

from frame.frames.party.fPlay import FPlay
from frame.frames.settings.fSettings import FSettings

class FMain(IFrame):

    def __init__(self):
        super().__init__()

    def draw(self):
        root = rootManager.getRoot()
        dimensions = super().getScreenDimensions(root)

        l1 = super().createLabel(master = root, text=rootManager.GAME_NAME, fontSize = 50)
        l1["fg"] = "lightblue"
        l1.pack()

        f1 = super().createFrame(root)
        f1.pack()


        b1 = super().createButton(master = f1 ,text="Jouer", cmd=lambda:rootManager.runNewFrame(FPlay(self)), fontSize=18)
        b1["bg"] = "blue"
        b1["fg"] = "#111111"
        b1.pack()

        b2 = super().createButton(master = f1, text="Options", cmd=lambda:rootManager.runNewFrame(FSettings(self)), fontSize=18)
        b2["bg"] = "green"
        b2["fg"] = "#111111"
        b2.pack()

        b3 = super().createButton(text="Quitter", cmd=lambda:rootManager.destroyRoot(), fontSize=18)
        b3["bg"] = "red"
        b3["fg"] = "#111111"
        b3.pack()
