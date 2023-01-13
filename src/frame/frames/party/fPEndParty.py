import frame.rootManager as rootManager

from frame.iFrame import IFrame

import utils.tkinter.tkUtils as tkUtils

import player.playerManager as playerManager

class FPEndParty(IFrame):
    """
    Montre à l'utilisateur qui est le robot qui a gagné
    et lui propose de revenir au menu principal
    """

    def __init__(self, previousFrame, playerWinner):
        super().__init__(previousFrame)
        self.playerWinner = playerWinner

    def draw(self):
        root = rootManager.getRoot()

        # Label du gagnant
        labelWinnerRobot = super().createLabel(text=f"Le gagnant est le numero {self.playerWinner.getID() + 1} !", fontSize=20)
        labelWinnerRobot.pack(pady=tkUtils.ratioHeight(0.01, root))

        # Icon du gagnant
        canvasPlayerIcon = super().createCanvas(width=playerManager.PLAYER_ICON_DIMENSIONS[0], height=playerManager.PLAYER_ICON_DIMENSIONS[1])
        canvasPlayerIcon.create_image((playerManager.PLAYER_ICON_DIMENSIONS[0] // 2) + 1, (playerManager.PLAYER_ICON_DIMENSIONS[1] // 2) + 1, image=self.playerWinner.getRobotIconTk())
        canvasPlayerIcon.pack(pady=tkUtils.ratioHeight(0.01, root))

        # Button retour
        buttonBack = super().createButton(text="Menu principal", cmd=lambda:rootManager.runNewFrame(rootManager.mainFrame))
        buttonBack.pack(pady=tkUtils.ratioHeight(0.01, root))
