import tkinter as tk

import frame.rootManager as rootManager
import utils.tkinter.tkUtils as tkUtils

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FCONFIGROBOT

from frame.frames.settings.robot.fCreateRobot import FCreateRobot
from frame.frames.settings.robot.fEditRobot import FEditRobot
from frame.frames.settings.robot.fDeleteRobot import FDeleteRobot

class FConfigRobot(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FCONFIGROBOT)

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        labelTitle = super().createLabel(master=root, text="Configuration des robots", fontSize=30)
        labelTitle.pack(side="top")

        frameMainButtons = super().createFrame(root)
        frameMainButtons.pack(pady=tkUtils.ratioHeight(0.1, root))

        buttonCreateRobot = super().createButton(master=frameMainButtons, text="Créer robot", cmd=lambda:rootManager.runNewFrame(FCreateRobot(self)))
        buttonCreateRobot.pack(pady = tkUtils.ratioHeight(0.02, root), fill=tk.X)

        buttonEditRobot = super().createButton(master=frameMainButtons,text="Editer robot", cmd=lambda:rootManager.runNewFrame(FEditRobot(self)))
        buttonEditRobot.pack(pady = tkUtils.ratioHeight(0.02, root), fill=tk.X)

        buttonDeleteRobot = super().createButton(master=frameMainButtons,text="Supprimer robot", cmd=lambda:rootManager.runNewFrame(FDeleteRobot(self)))
        buttonDeleteRobot.pack(pady = tkUtils.ratioHeight(0.02, root), fill=tk.X)

        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FConfigRobot, self).reopenLastFrame())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)
