import tkinter as tk

import frame.rootManager as rootManager
import player.playerManager as playerManager

import utils.tkinter.tkUtils as tkUtils
from frame.messagesHelp import HELP_FPPARTYCONFIG
from frame.iFrame import IFrame
from frame.frames.party.fPMapConfig import FPMapConfig

class FPPartyConfig(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FPPARTYCONFIG)

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        labelTitle = super().createLabel(master=root, text="Paramètres de partie", fontSize=30)
        labelTitle.pack()

        frameMain = super().createFrame(root)
        frameMain.pack(pady = tkUtils.ratioHeight(0.04, root))

        self.scalebarEnergy = super().createScalebar(master=frameMain, text="Energie pour chaque robot", from_=500, to=3000, defaultValue=1000, length=600, tickInterval=250, resolution=50)
        self.scalebarEnergy.pack(pady = tkUtils.ratioHeight(0.01, root), fill=tk.X)

        self.scalebarDetection = super().createScalebar(master=frameMain, text="Distance de détection", from_=3, to=6, defaultValue=4, length=600, tickInterval=1, resolution=1)
        self.scalebarDetection.pack(pady = tkUtils.ratioHeight(0.01, root), fill=tk.X)

        # Confirmer
        buttonConfirm = super().createButton(master=frameMain, text="Configuration de la map", cmd=lambda:self.followingFrame())
        buttonConfirm.pack(pady = tkUtils.ratioHeight(0.04, root), fill=tk.X)

        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FPPartyConfig, self).reopenLastFrame())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

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
