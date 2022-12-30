import frame.rootManager as rootManager

import tkinter as tk
from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FCONFIGMAP

from frame.frames.settings.map.fCreateMap import FCreateMap
from frame.frames.settings.map.fEditMap import FEditMap
from frame.frames.settings.map.fDeleteMap import FDeleteMap

class FConfigMap(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FCONFIGMAP)

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        labelTitle = super().createLabel(master=root, text="Configuration de la carte", fontSize=30)
        labelTitle.pack(side="top")

        frameMainButtons = super().createFrame(root)
        frameMainButtons.pack(pady=100)

        buttonCreateNewMap = super().createButton(master=frameMainButtons, text="Créer une map", cmd=lambda: rootManager.runNewFrame(FCreateMap(self)))
        buttonCreateNewMap.pack(pady = 15, fill=tk.X)

        buttonEditMap = super().createButton(master=frameMainButtons, text="Editer une map", cmd=lambda:rootManager.runNewFrame(FEditMap(self)))
        buttonEditMap.pack(pady = 15, fill=tk.X)

        buttonDeleteMap = super().createButton(master=frameMainButtons, text="Supprimer une map", cmd=lambda:rootManager.runNewFrame(FDeleteMap(self)))
        buttonDeleteMap.pack(pady = 15, fill=tk.X)

        buttonBack = super().createButton(text="Retour", cmd=super(FConfigMap, self).reopenLastFrame)
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)
