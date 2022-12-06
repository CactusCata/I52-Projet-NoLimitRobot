import frame.rootManager as rootManager

from frame.iFrame import IFrame

from frame.frames.settings.map.fCreateMap import FCreateMap
from frame.frames.settings.map.fEditMap import FEditMap
from frame.frames.settings.map.fDeleteMap import FDeleteMap

class FConfigMap(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()

        buttonCreateNewMap = super().createButton(text="Créer une map", cmd=lambda: rootManager.runNewFrame(FCreateMap(self)))
        buttonCreateNewMap.pack()

        buttonEditMap = super().createButton(text="Editer une map", cmd=lambda:rootManager.runNewFrame(FEditMap(self)))
        buttonEditMap.pack()

        buttonDeleteMap = super().createButton(text="Supprimer une map", cmd=lambda:rootManager.runNewFrame(FDeleteMap(self)))
        buttonDeleteMap.pack()

        buttonReturn = super().createButton(text="Retour", cmd=lambda:super(FConfigMap, self).reopenLastFrame())
        buttonReturn.pack()

        buttonHelp = super().createButton(text="Aide")
        buttonHelp.pack()
