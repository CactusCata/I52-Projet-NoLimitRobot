import map.mapManager as mapManager
from tkinter import messagebox

from frame.iFrame import IFrame

class FDeleteMap(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        mapNameLabel = super().createLabel(text="Nom de la map:")
        mapNameLabel.pack()

        self.mapNameComboBox = super().createComboBox(list=mapManager.getLoadedMaps())
        self.mapNameComboBox.pack()

        confirmButton = super().createButton(text="Supprimer", cmd=lambda:self.confirmButtonAction())
        confirmButton.pack()

        helpButton = super().createButton(text="Aide")
        helpButton.pack()

        returnButton = super().createButton(text="Retour", cmd=lambda:super(FDeleteMap, self).reopenLastFrame())
        returnButton.pack()

    def confirmButtonAction(self):
        selectedMapName = self.mapNameComboBox.get()

        messagebox.showinfo(title="Information", message=f"La map {selectedMapName} a bien été supprimée")
        mapManager.deleteMap(selectedMapName)

        super(FDeleteMap, self).reopenLastFrame()
    
