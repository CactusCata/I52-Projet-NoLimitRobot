import frame.rootManager as rootManager

import tkinter as tk
from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FCONFIGMAP

import utils.tkinter.tkUtils as tkUtils

from frame.frames.settings.map.fCreateMap import FCreateMap
from frame.frames.settings.map.fEditMap import FEditMap
from frame.frames.settings.map.fDeleteMap import FDeleteMap

class FConfigMap(IFrame):
    """
    Propose à l'utilisateur de:
        - Créer une carte
        - Editer une carte
        - Supprimer une carte
    """

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FCONFIGMAP)

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        labelTitle = super().createLabel(master=root, text="Configuration de la carte", fontSize=30)
        labelTitle.pack(side="top")

        frameMainButtons = super().createFrame(root)
        frameMainButtons.pack(pady=tkUtils.ratioHeight(0.1, root))

        # Créer carte
        buttonCreateNewMap = super().createButton(master=frameMainButtons, text="Créer une map", cmd=lambda: rootManager.runNewFrame(FCreateMap(self)))
        buttonCreateNewMap.pack(pady=tkUtils.ratioHeight(0.02, root), fill=tk.X)

        # Editer carte
        buttonEditMap = super().createButton(master=frameMainButtons, text="Editer une map", cmd=lambda:rootManager.runNewFrame(FEditMap(self)))
        buttonEditMap.pack(pady=tkUtils.ratioHeight(0.02, root), fill=tk.X)

        # Supprimer carte
        buttonDeleteMap = super().createButton(master=frameMainButtons, text="Supprimer une map", cmd=lambda:rootManager.runNewFrame(FDeleteMap(self)))
        buttonDeleteMap.pack(pady=tkUtils.ratioHeight(0.02, root), fill=tk.X)

        # Retour
        buttonBack = super().createButton(text="Retour", cmd=super(FConfigMap, self).reopenLastFrame)
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)
