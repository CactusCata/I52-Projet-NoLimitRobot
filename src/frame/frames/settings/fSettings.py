import tkinter as tk

import frame.rootManager as rootManager
from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FSETTINGS
import param.paramManager as paramManager

import utils.tkinter.tkUtils as tkUtils

from frame.frames.settings.map.fConfigMap import FConfigMap
from frame.frames.settings.robot.fConfigRobot import FConfigRobot
from frame.frames.settings.party.fDeleteParty import FDeleteParty

class FSettings(IFrame):
    """
    Propose à l'utilisateur de:
        - Configurer les cartes
        - Configurer les robots
        - Supprimer les parties
        - Mettre en plein écran
        - Proposer de l'aide
    """

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FSETTINGS)

        # Permet de cocher ou non les CheckButtons associés
        self.fullScreenTickedVar = None
        self.needHelpTickedVar = None

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        frameTitle = super().createFrame(root)
        frameTitle.pack(side="top")

        frameMainButtons = super().createFrame(root)
        frameMainButtons.pack(pady=tkUtils.ratioHeight(0.04, root))

        labelTitle = super().createLabel(master=frameTitle, text="Options", fontSize=30)
        labelTitle.pack()

        # Configuration des maps
        buttonConfigMap = super().createButton(master=frameMainButtons, text="Configuration des maps", cmd=lambda:rootManager.runNewFrame(FConfigMap(self)))
        buttonConfigMap.pack(pady=tkUtils.ratioHeight(0.01, root), fill=tk.X)

        # Configuration des robots
        buttonConfigRobot = super().createButton(master=frameMainButtons, text="Configuration des robots", cmd=lambda:rootManager.runNewFrame(FConfigRobot(self)))
        buttonConfigRobot.pack(pady=tkUtils.ratioHeight(0.01, root), fill=tk.X)

        # Suppression d'une partie
        buttonDeleteParty = super().createButton(master=frameMainButtons, text="Supprimer une partie", cmd=lambda:rootManager.runNewFrame(FDeleteParty(self)))
        buttonDeleteParty.pack(pady=tkUtils.ratioHeight(0.01, root), fill=tk.X)

        # Plein écran
        self.fullScreenTickedVar = tk.IntVar(value=int(paramManager.PARAM.getFullScreenState()))
        comboBoxFullScreen = super().createCheckButton(master=frameMainButtons, text="Plein ecran", variable=self.fullScreenTickedVar, callback=lambda:self.toggleFullScreen())
        comboBoxFullScreen.pack(pady = tkUtils.ratioHeight(0.01, root), fill=tk.X)

        # Bouton d'aide
        self.needHelpTickedVar = tk.IntVar(value=int(paramManager.PARAM.isNeedHelp()))
        comboBoxEnableHelp = super().createCheckButton(master=frameMainButtons, text="Activer l'aide", variable=self.needHelpTickedVar, callback=lambda:self.toggleHelp())
        comboBoxEnableHelp.pack(pady = tkUtils.ratioHeight(0.02, root), fill=tk.X)


        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FSettings, self).reopenLastFrame())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

    def updateWidgetsPlacement(self):
        """
        Si le plein écran est modifié, on doit
        redisposer les widgets de la fenêtre actuelle
        """
        super().clearFrame()
        self.draw()

    def toggleFullScreen(self):
        paramManager.PARAM.toggleFullScreen(rootManager.getRoot())
        self.updateWidgetsPlacement()

    def toggleHelp(self):
        paramManager.PARAM.toggleHelp()
