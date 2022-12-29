import tkinter as tk
from tkinter import messagebox

import frame.rootManager as rootManager
import map.mapManager as mapManager


from frame.iFrame import IFrame, help_activated
from frame.messagesHelp import HELP_FCREATEMAP

class FCreateMap(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()

        if help_activated == True:
            buttonHelp = super().createButtonHelp(master = root, msg=HELP_FCREATEMAP)
            super().modifyButton(buttonHelp ,bg = "darkgreen", ab = "green")
            buttonHelp.pack(anchor = "e", padx = 10, pady = 10)

        labelTitle = super().createLabel(master=root, text="Création de la carte", fontSize=30)
        labelTitle.pack(side="top")

        frameMainButtons = super().createFrame(root)
        frameMainButtons.pack(pady=100)

        labelNameMap = super().createLabel(master=frameMainButtons, text="Nom de la map:")
        labelNameMap.pack(fill=tk.X)

        self.textboxNameMap = super().createTextBox(master=frameMainButtons)
        self.textboxNameMap.pack(pady = 15, fill=tk.X)

        confirmButton = super().createButton(master=frameMainButtons, text="Confirmer", cmd=lambda:self.confirmButtonAction())
        confirmButton.pack(pady = 15, fill=tk.X)


        buttonBack = super().createButton(text="Retour", cmd=super(FCreateMap, self).reopenLastFrame)
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

    def confirmButtonAction(self):
        wantedMapName = self.mapNameTextBox.get("1.0", "end").rstrip()

        if wantedMapName in mapManager.getLoadedMaps():
            messagebox.showerror(title="Erreur", message="Ce nom de map existe déjà !")
            return

        mapManager.createNewMap(wantedMapName)
        super(FCreateMap, self).reopenLastFrame()
