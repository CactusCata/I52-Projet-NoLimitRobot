from tkinter import Frame, BOTH

import frame.rootManager as rootManager
import utils.tkUtils as tkUtils

from frame.iFrame import IFrame

from frame.frames.party.fPlay import FPlay
from frame.frames.settings.fSettings import FSettings

class FMain(IFrame):

    def __init__(self):
        super().__init__()

    def draw(self):
        root = rootManager.getRoot()

        l1 = super().createLabel(text=rootManager.GAME_NAME)
        l1.pack()

        b1 = super().createButton(text="Jouer", cmd=lambda:rootManager.runNewFrame(FPlay(self)), fontSize=18)
        b1.pack()

        b2 = super().createButton(text="Options", cmd=lambda:rootManager.runNewFrame(FSettings(self)), fontSize=18)
        b2.pack()

        b3 = super().createButton(text="Quitter", cmd=lambda:rootManager.destroyRoot(), fontSize=18)
        b3.pack()