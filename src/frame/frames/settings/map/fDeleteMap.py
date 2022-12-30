import tkinter as tk
from tkinter import messagebox

import frame.rootManager as rootManager
import map.mapManager as mapManager

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
        frameMainButtons.pack(pady=100)

        labelNameMap = super().createLabel(text="Nom de la map:")
        labelNameMap.pack()

        self.mapNameComboBox = super().createComboBox(list=mapManager.getLoadedMaps())
        self.mapNameComboBox.pack()

        confirmButton = super().createButton(text="Supprimer", cmd=lambda:self.confirmButtonAction())
        confirmButton.pack()


        returnButton = super().createButton(text="Retour", cmd=lambda:super(FDeleteMap, self).reopenLastFrame())
        returnButton.pack()

    def confirmButtonAction(self):
        selectedMapName = self.mapNameComboBox.get()

        messagebox.showinfo(title="Information", message=f"La map {selectedMapName} a bien été supprimée")
        mapManager.deleteMap(selectedMapName)

        super(FDeleteMap, self).reopenLastFrame()
