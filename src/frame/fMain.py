from tkinter import Frame, BOTH

import frame.rootManager as rootManager
import utils.tkUtils as tkUtils

from frame.iFrame import IFrame

from frame.fTest import FTest
#from fSetting import FSetting

class FMain(IFrame):

    def draw(self):
        root = rootManager.getRoot()

        b1 = super().createButton(text="Jouer", cmd=self.playButtonAction, fontSize=18)
        tkUtils.packRelativeRatio(root, b1, 0.2, 0.2, "w")

        b2 = super().createButton(text="Options", cmd=self.settingButtonAction, fontSize=18)
        tkUtils.packRelativeRatio(root, b2, 0.2, 0.05, "w")

        b3 = super().createButton(text="Quitter", cmd=rootManager.destroyRoot, fontSize=18)
        tkUtils.packRelativeRatio(root, b3, 0.2, 0.05, "w")


    def playButtonAction(self):
        rootManager.clearCurrentFrame()
        rootManager.runNewFrame(FTest())

    def settingButtonAction(self):
        pass
