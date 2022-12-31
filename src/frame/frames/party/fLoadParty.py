import frame.rootManager as rootManager

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FLOADPARTY

class FLoadParty(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FLOADPARTY)

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FLoadParty, self).reopenLastFrame())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)
