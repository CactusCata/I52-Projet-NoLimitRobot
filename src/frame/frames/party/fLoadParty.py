import frame.rootManager as rootManager

from frame.iFrame import IFrame

class FLoadParty(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame, "AIDE")

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        b4 = super().createButton(text="Retour", cmd=lambda:super(FLoadParty, self).reopenLastFrame())
        b4.pack()