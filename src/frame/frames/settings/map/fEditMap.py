import frame.rootManager as rootManager
import map.mapManager as mapManager
from map.mapManager import MAP_MAX_ROCK_AMOUNT
import image.imageManager as imageManager

from utils.tkinter.tkPerformer import TkPerformer

from tkinter import StringVar

from map.mapDrawer import MapDrawer

from frame.iFrame import IFrame, help_activated
from frame.messagesHelp import HELP_FEDITMAP

from random import uniform, randint

class FEditMap(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

        self.map = None
        self.mapName = None
        self.mapDrawer = None

        self.currentMapHasChanged = False

    def draw(self):
        root = rootManager.getRoot()

        # Choix de la map
        labelMapName = super().createLabel(text="Choisir la map:")
        labelMapName.place(x=10, y=10)
        self.comboBoxMapName = super().createComboBox(list=mapManager.getLoadedMaps(), callback=lambda event: self.mapSelectedChanged(event))
        self.comboBoxMapName.place(x=10, y=40)

        # Map
        self.canvasMap = super().createCanvas(width=700, height=500)
        self.canvasMap.place(x=300, y=10)

        # Choix du bloc
        self.stringVarRadioButton = StringVar()
        self.stringVarRadioButton.set("Air")
        self.radioButtonBlockAir = super().createRadioButton(text="Air", serializedValue="AIR", variable=self.stringVarRadioButton, callback=lambda:self.radioButtonChanged())
        self.radioButtonBlockAir.select()
        self.radioButtonBlockAir.place(x=10, y=100)
        self.radioButtonBlockRock = super().createRadioButton(text="Rock", serializedValue="ROCK", variable=self.stringVarRadioButton, callback=lambda: self.radioButtonChanged())
        self.radioButtonBlockRock.place(x=10, y=140)

        self.canvasMap.bind("<Button-1>", lambda eventClick:self.clickAndMoveMouseEvent(eventClick.x, eventClick.y))

        # Nombre de rocher actuel
        self.labelRockAmount = super().createLabel(text=f"Nombre de rocher {0}/{MAP_MAX_ROCK_AMOUNT}")
        self.labelRockAmount.place(x=10, y=300)

        # scalebar du pourcentage de rocher aléatoire
        self.scalebarRandomRock = super().createScalebar(text="Pourcentage de rocher aléatoire", from_=0, to=20, defaultValue=5, length=300, tickInterval=5, resolution=1, callback=lambda event: self.scalebarChangeEvent(event))
        self.scalebarRandomRock.place(x=1050, y=50)

        # bouton pour regenerer une map avec le pourcentage
        # de rocher de la scalebar
        self.buttonRegenerateRandomMap = super().createButton(text="Regenerer la map", cmd=lambda:self.scalebarChangeEvent(None))
        self.buttonRegenerateRandomMap.place(x=1050, y=400)

        # Bouton de sauvegarde de l'état de la map
        self.buttonSaveMap = super().createButton(text="Sauvegarder", cmd=lambda:self.saveMap())
        self.buttonSaveMap['state'] = "disabled"
        self.buttonSaveMap.place(x=1050, y=500)

        if help_activated == True:
            buttonHelp = super().createButtonHelp(master = root, msg=HELP_FEDITMAP)
            buttonHelp.place(x=1050, y=550)

        buttonReturn = super().createButton(text="Retour", cmd=lambda:self.tryToReopenLastFrame())
        buttonReturn.place(x=1050, y=600)

    def scalebarChangeEvent(self, event):
        """
        Evenement déclanché lorsque le curseur de la scale bar est changé
        """
        if (self.map != None):
            percentageOfRock = self.scalebarRandomRock.get()
            self.regenerateMap(percentageOfRock)

            # Mise à jour graphique de la map
            self.mapDrawer.clear()
            self.mapDrawer.drawMap()
            self.mapDrawer.drawGrid()

            # Mise à jour du label qui compte les rochers
            self.updateRockAmountLabel()

            # Proposer de sauvegarder l'état de la map
            self.buttonSaveMap['state'] = "normal"
            self.currentMapHasChanged = True
        

    def updateRockAmountLabel(self):
        """
        Met à jour le label qui compte le nombre de rocher sur la map
        """
        self.labelRockAmount["text"] = f"Nombre de rocher {self.map.getRockAmount()}/{MAP_MAX_ROCK_AMOUNT}"

        if (self.labelRockAmount["fg"] == "#FF0000" and self.map.getRockAmount() <= MAP_MAX_ROCK_AMOUNT):
            self.labelRockAmount["fg"] = '#ABB2B9'
        elif (self.labelRockAmount["fg"] == "#ABB2B9" and self.map.getRockAmount() > MAP_MAX_ROCK_AMOUNT):
            self.labelRockAmount["fg"] = '#FF0000'
            self.buttonSaveMap["state"] = "disabled"

    def regenerateMap(self, percentageOfRock):
        """
        Genere une nouvelle map selon une proportion de bloc
        et met l'affichage à jour
        """
        # Supprime tous les éléments de la map (met du vide partout)
        self.map.clear()

        # On rempli bien la map de rocher, même plus que ce qu'il n'en faut parfois
        # pour éviter que le bas de la carte n'ai pas de rocher
        rockAmountNeeded = int((percentageOfRock / 100) * self.map.getDimX() * self.map.getDimY())
        rocksPlaces = []
        while (self.map.getRockAmount() < rockAmountNeeded):
            for x in range(self.map.getDimX()):
                for y in range(self.map.getDimY()):
                    if self.map.getID(x, y) != 1: # Si un rocher n'est pas présent
                        if uniform(0, 1) * 100 < percentageOfRock: # on essaye d'en placer un
                            if (self.map.placeRock(x, y)):
                                rocksPlaces.append((x, y))
                        else: # il y aura une case d'air, mais on doit vérifier si l'air peut légalement être là, si ce n'est pas le cas, on ajoute un bloc de roche
                            if (not self.map.canPlaceAir(x, y)):
                                self.map.placeRock(x, y)
                                rocksPlaces.append((x, y))

        # On supprime les rochers superflu s'il y en a
        n = len(rocksPlaces) - 1
        while (self.map.getRockAmount() > rockAmountNeeded):
            randomRockPos = rocksPlaces[randint(0, n)]
            self.map.placeAir(randomRockPos[0], randomRockPos[1])

    def clickAndMoveMouseEvent(self, x1, y1):
        """
        Evenement déclanché lorsque l'utilisateur clique sur le canvas
        """

        ids = self.canvasMap.find_withtag("current")

        # Ne pas traiter le cas où il n'y a pas d'élément à inspecter
        if (len(ids) == 0):
            return

        id = ids[0] # id de l'élément sur la souris
        itemCoordinates = self.mapDrawer.getItemCoordinates(id)

        if (itemCoordinates == None):
            return

        x = itemCoordinates[0]
        y = itemCoordinates[1]

        img = None
        if (self.stringVarRadioButton.get() == "ROCK" and self.map.getID(x, y) != 1):
            if self.map.placeRock(x, y):
                img = imageManager.IMG_MAP_ROCK_TK
        elif (self.stringVarRadioButton.get() == "AIR" and self.map.getData(x, y) != 0):
            if (self.map.placeAir(x, y)):
                img = imageManager.IMG_MAP_AIR_TK

        if (img != None): # Si le bloc a changé, alors on supprime l'ancien bloc et on dessine le nouveau
            self.currentMapHasChanged = True
            self.updateRockAmountLabel()
            self.canvasMap.delete(id)
            self.mapDrawer.drawImage(img, x, y, tag=f"figure:{x},{y}")

            # Mise à jour de l'état du bouton en fonction de la quantité de rocher
            if (self.map.getRockAmount() > MAP_MAX_ROCK_AMOUNT):
                self.buttonSaveMap['state'] = "disabled"
            else:
                self.buttonSaveMap['state'] = "normal"

    def radioButtonChanged(self):
        """
        Evenement déclanché lorsque l'utilisateur change l'état du radio button
        """
        print("value changed")
        print(self.stringVarRadioButton.get())

    def mapSelectedChanged(self, event):
        """
        Evenement déclanché lorsque l'utilisateur choisi une carte
        """

        # Nom de la carte sélectionnée
        currentMapName = self.comboBoxMapName.get()

        if (self.currentMapHasChanged and self.mapName != currentMapName):
            returnCode = TkPerformer(rootManager.getRoot(), "Editeur de map", "Voulez-vous sauvegarder les modifications ?").run()
            if (returnCode == 0):
                self.saveMap()
            elif (returnCode == 2):
                self.comboBoxMapName.current(self.comboBoxMapName.current())
                return

        self.mapName = self.comboBoxMapName.get()

        # object map associé
        self.map = mapManager.loadMapFileContent(self.mapName)
        self.updateRockAmountLabel()

        self.mapDrawer = MapDrawer(self.canvasMap, self.map)
        self.mapDrawer.drawMap()
        self.mapDrawer.drawGrid()

    def saveMap(self):
        """
        Sauvegarde l'état actuel de la map
        """
        mapManager.saveMap(self.mapName, self.map)
        self.buttonSaveMap['state'] = "disabled"
        self.currentMapHasChanged = False

    def tryToReopenLastFrame(self):

        if (self.currentMapHasChanged):
            returnCode = TkPerformer(rootManager.getRoot(), "Editeur de map", "Voulez-vous sauvegarder les modifications ?").run()
            if (returnCode == 0):
                self.saveMap()
            elif (returnCode == 1):
                return

        super(FEditMap, self).reopenLastFrame()
