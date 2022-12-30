
import tkinter as tk

import frame.rootManager as rootManager
from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FSETTINGS
import param.paramManager as paramManager

import time

from frame.frames.settings.map.fConfigMap import FConfigMap
from frame.frames.settings.robot.fConfigRobot import FConfigRobot
from frame.frames.settings.party.fDeleteParty import FDeleteParty

class FSettings(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FSETTINGS)

        self.fullScreenTickedVar = None
        self.needHelpTickedVar = None

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        frameTitle = super().createFrame(root)
        frameTitle.pack(side="top")

        frameMainButtons = super().createFrame(root)
        frameMainButtons.pack(pady=100)

        labelTitle = super().createLabel(master=frameTitle, text="Options", fontSize=30)
        labelTitle.pack()


        buttonConfigMap = super().createButton(master=frameMainButtons, text="Configuration des maps", cmd=lambda:rootManager.runNewFrame(FConfigMap(self)))
        buttonConfigMap.pack(pady = 15, fill=tk.X)

        buttonConfigRobot = super().createButton(master=frameMainButtons, text="Configuration des robots", cmd=lambda:rootManager.runNewFrame(FConfigRobot(self)))
        buttonConfigRobot.pack(pady = 15, fill=tk.X)

        buttonDeleteParty = super().createButton(master=frameMainButtons, text="Supprimer une partie", cmd=lambda:rootManager.runNewFrame(FDeleteParty(self)))
        buttonDeleteParty.pack(pady = 15, fill=tk.X)

        self.fullScreenTickedVar = tk.IntVar(value=int(paramManager.PARAM.getFullScreenState()))
        comboBoxFullScreen = super().createCheckButton(master=frameMainButtons, text="Plein ecran", variable=self.fullScreenTickedVar, callback=lambda:self.toggleFullScreen())
            #comboBoxFullScreen["state"] = "selected"
        comboBoxFullScreen.pack(pady = 15, fill=tk.X)

        self.needHelpTickedVar = tk.IntVar(value=int(paramManager.PARAM.isNeedHelp()))
        comboBoxEnableHelp = super().createCheckButton(master=frameMainButtons, text="Activer l'aide", variable=self.needHelpTickedVar, callback=lambda:self.toggleHelp())
        #comboBoxEnableHelp["bd"] = 4
        comboBoxEnableHelp.pack(pady = 30, fill=tk.X)


        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FSettings, self).reopenLastFrame())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

    def updateWidgetsPlacement(self):
        super().clearFrame()
        self.draw()

    def toggleFullScreen(self):
        paramManager.PARAM.toggleFullScreen(rootManager.getRoot())
        self.updateWidgetsPlacement()

    def toggleHelp(self):
        paramManager.PARAM.toggleHelp()
