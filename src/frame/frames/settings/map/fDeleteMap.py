import tkinter as tk
from tkinter import messagebox

import frame.rootManager as rootManager
import map.mapManager as mapManager

import utils.tkinter.tkUtils as tkUtils

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FDELETEMAP

class FDeleteMap(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FDELETEMAP)

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        labelTitle = super().createLabel(root)
        labelTitle.pack(side="top")

        frameMainButtons = super().createFrame(root)
        frameMainButtons.pack(pady=tkUtils.ratioHeight(0.1, root))

        labelNameMap = super().createLabel(text="Nom de la map:")
        labelNameMap.pack(pady=tkUtils.ratioHeight(0.02, root))

        self.mapNameComboBox = super().createComboBox(list=mapManager.getLoadedMaps())
        self.mapNameComboBox.pack()

        buttonConfirm = super().createButton(text="Supprimer", cmd=lambda:self.confirmButtonAction())
        buttonConfirm.pack(pady=tkUtils.ratioHeight(0.02, root))

        buttonBack = super().createButton(text="Retour", cmd=super(FDeleteMap, self).reopenLastFrame)
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

    def confirmButtonAction(self):
        selectedMapName = self.mapNameComboBox.get()

        messagebox.showinfo(title="Information", message=f"La map {selectedMapName} a bien été supprimée")
        mapManager.deleteMap(selectedMapName)

        super(FDeleteMap, self).reopenLastFrame()
