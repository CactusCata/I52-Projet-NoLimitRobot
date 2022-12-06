import frame.rootManager as rootManager

from frame.iFrame import IFrame

class FLoadParty(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()

        b3 = super().createButton(text="Aide")
        b3.pack()

        b4 = super().createButton(text="Retour", cmd=lambda:super(FLoadParty, self).reopenLastFrame())
        b4.pack()