import frame.rootManager as rootManager

from frame.iFrame import IFrame

from frame.frames.party.fPPlayerConfig import FPPlayerConfig
from frame.frames.party.fLoadParty import FLoadParty

class FPlay(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()

        b1 = super().createButton(text="Nouvelle partie", cmd=lambda: rootManager.runNewFrame(FPPlayerConfig(self)))
        b1.pack()

        b2 = super().createButton(text="Charger partie", cmd=lambda:rootManager.runNewFrame(FLoadParty(self)))
        b2.pack()

        b3 = super().createButton(text="Aide")
        b3.pack()

        b4 = super().createButton(text="Retour", cmd=lambda:super(FPlay, self).reopenLastFrame())
        b4.pack()