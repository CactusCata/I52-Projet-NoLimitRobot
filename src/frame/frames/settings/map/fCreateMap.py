import frame.rootManager as rootManager
import map.mapManager as mapManager

from tkinter import messagebox

from frame.iFrame import IFrame, help_activated
from frame.messagesHelp import HELP_FCREATEMAP

class FCreateMap(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()
        
        mapNameLabel = super().createLabel(text="Nom de la map:")
        mapNameLabel.pack()

        self.mapNameTextBox = super().createTextBox()
        self.mapNameTextBox.pack()

        confirmButton = super().createButton(text="Confirmer", cmd=lambda:self.confirmButtonAction())
        confirmButton.pack()

        if help_activated == True:
            helpButton = super().createButtonHelp(master = root, msg=HELP_FCREATEMAP)
            helpButton.pack()

        returnButton = super().createButton(text="Retour", cmd=super().reopenLastFrame)
        returnButton.pack()

    def confirmButtonAction(self):
        wantedMapName = self.mapNameTextBox.get("1.0", "end").rstrip()

        if wantedMapName in mapManager.getLoadedMaps():
            messagebox.showerror(title="Erreur", message="Ce nom de map existe déjà !")
            return

        mapManager.createNewMap(wantedMapName)
        super(FCreateMap, self).reopenLastFrame()
