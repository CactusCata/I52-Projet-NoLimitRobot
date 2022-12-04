from tkinter import Frame

import frame.rootManager as rootManager

from frame.iFrame import IFrame

from frame.fTest import FTest
#from fSetting import FSetting

class FMain(IFrame):

    def draw(self):
        root = rootManager.getRoot()

        frameB1 = Frame(root, bg='#1E1E1E')
        b1 = super().createButton(master=frameB1, text="Jouer", cmd=self.playButtonAction)
        b1.pack()
        frameB1.pack()

        b2 = super().createButton(text="Options", cmd=self.settingButtonAction)
        b2.pack()

        b3 = super().createButton(text="Quitter", cmd=rootManager.destroyRoot)
        b3.pack()


    def playButtonAction(self):
        rootManager.clearCurrentFrame()
        rootManager.runNewFrame(FTest())

    def settingButtonAction(self):
        pass
