import tkinter as tk
from tkinter import messagebox

import frame.rootManager as rootManager
import map.mapManager as mapManager

import utils.tkinter.tkUtils as tkUtils

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FCREATEMAP

class FCreateMap(IFrame):
    """
    Permet à l'utilisateur de créer une carte
    """

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FCREATEMAP)

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        labelTitle = super().createLabel(master=root, text="Création de la carte", fontSize=30)
        labelTitle.pack(side="top")

        frameMainButtons = super().createFrame(root)
        frameMainButtons.pack(pady=tkUtils.ratioHeight(0.1, root))

        labelNameMap = super().createLabel(master=frameMainButtons, text="Nom de la map:")
        labelNameMap.pack(fill=tk.X)

        # Nom de la carte
        self.textboxNameMap = super().createTextBox(master=frameMainButtons)
        self.textboxNameMap.pack(pady = tkUtils.ratioHeight(0.02, root), fill=tk.X)

        # Confirm
        confirmButton = super().createButton(master=frameMainButtons, text="Confirmer", cmd=lambda:self.confirmButtonAction())
        confirmButton.pack(pady = tkUtils.ratioHeight(0.02, root), fill=tk.X)

        # Retour
        buttonBack = super().createButton(text="Retour", cmd=super(FCreateMap, self).reopenLastFrame)
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

    def confirmButtonAction(self):
        """
        Méthode appelée lorsque l'utilisateur clic sur
        le bouton de confirmation de carte
        """
        wantedMapName = self.textboxNameMap.get("1.0", "end").rstrip()

        # Annuler si l'utilisateur n'a pas entré de nom de carte
        if (wantedMapName == ""):
            messagebox.showerror(title="Erreur", message="Veuillez entrer un nom de carte")
            return

        # Annuler la requete si une carte possède déjà le nom
        # demandé
        if wantedMapName in mapManager.getLoadedMaps():
            messagebox.showerror(title="Erreur", message="Ce nom de map existe déjà !")
            return

        mapManager.createNewMap(wantedMapName)
        super(FCreateMap, self).reopenLastFrame()
