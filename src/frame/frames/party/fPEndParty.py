import frame.rootManager as rootManager

from frame.iFrame import IFrame

import player.playerManager as playerManager

class FPEndParty(IFrame):

    def __init__(self, previousFrame, playerWinner):
        super().__init__(previousFrame)
        self.playerWinner = playerWinner

    def draw(self):
        root = rootManager.getRoot()

        labelWinnerRobot = super().createLabel(text=f"Le gagnant est le numero {self.playerWinner.getID()} !", fontSize=20)
        labelWinnerRobot.pack()

        canvasPlayerIcon = super().createCanvas(width=playerManager.PLAYER_ICON_DIMENSIONS[0], height=playerManager.PLAYER_ICON_DIMENSIONS[1])
        canvasPlayerIcon.create_image((playerManager.PLAYER_ICON_DIMENSIONS[0] // 2) + 1, (playerManager.PLAYER_ICON_DIMENSIONS[1] // 2) + 1, image=self.playerWinner.getRobotIconTk())
        canvasPlayerIcon.pack()

        # Retour
        buttonBack = super().createButton(text="Menu principal", cmd=lambda:rootManager.runNewFrame(rootManager.mainFrame))
        buttonBack.pack()
