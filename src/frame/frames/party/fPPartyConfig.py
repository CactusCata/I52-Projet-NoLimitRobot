import frame.rootManager as rootManager
import game.gameManager as gameManager

from frame.iFrame import IFrame
from frame.frames.party.fPMapConfig import FPMapConfig

class FPPartyConfig(IFrame):
    """
    Energie 'scroll bar'
    Distance de detection/repérage
    suivant
    retour
    aide
    """

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
        detectionDistance = int (self.scalebarDetection.get())

        gameManager.setEnergyPerRobot(energyPerRobot)
        gameManager.setRobotDistanceDetection(detectionDistance)

        rootManager.runNewFrame(FPMapConfig(self))
