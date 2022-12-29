
import tkinter as tk

import frame.rootManager as rootManager
from frame.iFrame import IFrame, help_activated
from frame.messagesHelp import HELP_FSETTINGS

from frame.frames.settings.map.fConfigMap import FConfigMap
from frame.frames.settings.robot.fConfigRobot import FConfigRobot
from frame.frames.settings.party.fDeleteParty import FDeleteParty

class FSettings(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()

        if help_activated == True:
            buttonHelp = super().createButtonHelp(master = root, msg=HELP_FSETTINGS)
            super().modifyButton(buttonHelp ,bg = "darkgreen", ab = "green")
            buttonHelp.pack(anchor = "e", padx = 10, pady = 10)

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

        #comboBoxFullScreen = super().createCheckButton(text="Plein ecran", callback=lambda:self.toggleFullScreen())
        #comboBoxFullScreen.pack()

        comboBoxEnableHelp = super().createCheckButton(master=frameMainButtons, text="Activer l'aide", callback=lambda:self.toggleHelp())
        #comboBoxEnableHelp["bd"] = 4
        comboBoxEnableHelp.pack(pady = 30, fill=tk.X)


        buttonBack = super().createButton(text="Retour", cmd=super(FSettings, self).reopenLastFrame)
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

    def toggleFullScreen(self):
        print("Fullscreen is toggled")

    def toggleHelp(self):
        print("Help has been toggled")
        global help_activated
        help_activated = False
