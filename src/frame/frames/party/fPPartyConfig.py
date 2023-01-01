import frame.rootManager as rootManager
import player.playerManager as playerManager

from frame.iFrame import IFrame
from frame.frames.party.fPMapConfig import FPMapConfig

class FPPartyConfig(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame, "AIDE")

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        self.scalebarEnergy = super().createScalebar(text="Energie pour chaque robot", from_=500, to=3000, defaultValue=1000, length=600, tickInterval=250, resolution=50)
        self.scalebarEnergy.pack()

        self.scalebarDetection = super().createScalebar(text="Distance de détection", from_=3, to=6, defaultValue=4, length=600, tickInterval=1, resolution=1)
        self.scalebarDetection.pack()

        # Confirmer
        buttonConfirm = super().createButton(text="Configuration de la map", cmd=lambda:self.followingFrame())
        buttonConfirm.pack()
        
        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FPPartyConfig, self).reopenLastFrame())
        buttonBack.pack()

    def followingFrame(self):
        """
        S'occupe de passer à la prochaine fenêtre ou non, en fonction des
        différentes erreurs présentes
        """
        energyPerRobot = int(self.scalebarEnergy.get())
        detectionDistance = int(self.scalebarDetection.get())

        for player in playerManager.PLAYER_LIST:
            playerRobot = player.getRobotParty()
            playerRobot.set_max_energy(energyPerRobot)
            playerRobot.reset_energy()
            playerRobot.set_detection_distance(detectionDistance)

        rootManager.runNewFrame(FPMapConfig(self))
