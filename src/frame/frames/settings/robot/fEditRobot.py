import frame.rootManager as rootManager

from frame.iFrame import IFrame

class FEditRobot(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()

        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FEditRobot, self).reopenLastFrame())
        buttonBack.pack()
