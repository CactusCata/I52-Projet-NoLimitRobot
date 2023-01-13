import frame.rootManager as rootManager

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FDELETEPARTY

class FDeleteParty(IFrame):
    """
    Permet à l'utilisateur de supprimer une partie.
    (Pas codé)
    """

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FDELETEPARTY)

    def draw(self):

        super().createButtonHelp()

        buttonBack = super().createButton(text="Retour", cmd=super(FDeleteParty, self).reopenLastFrame)
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)
