import frame.rootManager as rootManager

from frame.iFrame import IFrame

class FDeleteParty(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()
