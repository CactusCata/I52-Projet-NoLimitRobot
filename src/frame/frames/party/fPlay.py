import frame.rootManager as rootManager
import utils.tkinter.tkUtils as tkUtils

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FPLAY

from frame.frames.party.fPPlayerConfig import FPPlayerConfig
from frame.frames.party.fLoadParty import FLoadParty

class FPlay(IFrame):
    """
    Propose à l'utilisateur de commencer une nouvelle partie
    ou d'en charger une.
    """

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FPLAY)

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        labelTitle = super().createLabel(master=root, text="Selection de partie", fontSize=30)
        labelTitle.pack()

        frameMain = super().createFrame(root)
        frameMain.pack(pady=tkUtils.ratioHeight(0.03, root))

        buttonNewGame = super().createButton(master=frameMain, text="Nouvelle partie", cmd=lambda: rootManager.runNewFrame(FPPlayerConfig(self)))
        buttonNewGame.pack(pady=tkUtils.ratioHeight(0.02, root))

        buttonLoadGame = super().createButton(master=frameMain, text="Charger partie", cmd=lambda:rootManager.runNewFrame(FLoadParty(self)))
        buttonLoadGame.pack(pady=tkUtils.ratioHeight(0.02, root))

        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FPlay, self).reopenLastFrame())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)
