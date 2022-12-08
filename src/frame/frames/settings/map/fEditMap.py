import frame.rootManager as rootManager
import map.mapManager as mapManager
from map.mapManager import MAP_LINE_AMOUNT, MAP_COL_AMOUNT, MAP_MAX_ROCK_AMOUNT, MAP_MAX_ROCK_PERCENTAGE
import image.imageManager as imageManager

import utils.tkUtils as tkUtils

from tkinter import StringVar

from frame.iFrame import IFrame

from random import uniform, randint

class FEditMap(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

        self.map = None
        self.mapName = None

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

        self.scalebarRandomRock = super().createScalebar(text="Pourcentage de rocher aléatoire", from_=0, to=20, defaultValue=5, length=300, tickInterval=5, resolution=1, callback=lambda event: self.scalebarChangeEvent(event))
        self.scalebarRandomRock.place(x=1050, y=50)

        buttonHelp = super().createButton(text="Aide")
        buttonHelp.place(x=1050, y=550)

        buttonReturn = super().createButton(text="Retour", cmd=lambda:super(FEditMap, self).reopenLastFrame())
        buttonReturn.place(x=1050, y=600)

    def scalebarChangeEvent(self, event):
        """
        Evenement déclanché lorsque le curseur de la scale bar est changé
        """
        if (self.map != None):
            percentageOfRock = self.scalebarRandomRock.get()
            self.regenerateMap(percentageOfRock)
        

    def regenerateMap(self, percentageOfRock):
        """
        Genere une nouvelle map selon une proportion de bloc
        et met l'affichage à jour
        """
        # Supprime tous les éléments de la map (met du vide partout)
        self.map.clear()

        # On rempli bien la map de rocher, même plus que ce qu'il n'en faut parfois
        # pour éviter que le bas de la carte n'ai pas de rocher
        rockAmountNeeded = int((percentageOfRock / 100) * MAP_COL_AMOUNT * MAP_LINE_AMOUNT)
        rocksPlaces = []
        while (self.map.getRockAmount() < rockAmountNeeded):
            i = 0
            while i < MAP_LINE_AMOUNT:
                j = 0
                while j < MAP_COL_AMOUNT:
                    if self.map.get(i, j) != 1:
                        if uniform(0, 1) * 100 < percentageOfRock: # placement d'un bloc
                            if (self.map.placeRock(i, j)):
                                rocksPlaces.append((i, j))
                        else: # placement d'air
                            if (not self.map.canPlaceAir(i, j)):
                                self.map.placeRock(i, j)
                                rocksPlaces.append((i, j))
                    j += 1
                i += 1

        # On supprime les rochers superflu s'il y en a
        n = len(rocksPlaces) - 1
        while (self.map.getRockAmount() > rockAmountNeeded):
            randomRockPos = rocksPlaces[randint(0, n)]
            self.map.placeAir(randomRockPos[0], randomRockPos[1])

        # Suppression de tous les éléments 
        self.canvasMap.delete("all")
        self.drawGrid()

        # On met à jour le label
        self.labelRockAmount["text"] = f"Nombre de rocher {self.map.getRockAmount()}/{MAP_MAX_ROCK_AMOUNT}"


    def clickAndMoveMouseEvent(self, x1, y1):
        ids = self.canvasMap.find_withtag("current")
        if (len(ids) > 0):
            id = ids[0] # id de l'élément sur la souris
            tag = tkUtils.itemHasTag(self.canvasMap, id, tkUtils.startWithFunction, "figure")
            if (tag != None):
                figureCoordinates = self.getTagCoordinates(tag) # tag commencant par 'figure'
                line = int(figureCoordinates[0])
                col = int(figureCoordinates[1])

                img = None
                if (self.stringVarRadioButton.get() == "ROCK" and self.map.getMatrix()[line][col] != 1):
                    if self.map.placeRock(line, col):
                        img = imageManager.IMG_MAP_ROCK_TK
                        self.labelRockAmount["text"] = f"Nombre de rocher {self.map.getRockAmount()}/{MAP_MAX_ROCK_AMOUNT}"
                        if (self.map.getRockAmount() > int(0.2 * (20 * 30))):
                            self.labelRockAmount["fg"] = "#FF0000"
                elif (self.stringVarRadioButton.get() == "AIR" and self.map.getMatrix()[line][col] != 0):
                    if (self.map.placeAir(line, col)):
                        img = imageManager.IMG_MAP_AIR_TK
                        self.labelRockAmount["text"] = f"Nombre de rocher {self.map.getRockAmount()}/{MAP_MAX_ROCK_AMOUNT}"
                        if (self.labelRockAmount["fg"] == "#FF0000" and self.map.getRockAmount() <= MAP_MAX_ROCK_AMOUNT):
                            self.labelRockAmount["fg"] = "#000000"

                super().drawImage(canvas=self.canvasMap, image=img, posX=col*22 +21, posY=line*22 + 21, tag=f"figure:{line},{col}")

    def getTagCoordinates(self, tag):
        coordsInfo = tag.split(":")[1]
        line = coordsInfo.split(",")[0]
        col = coordsInfo.split(",")[1]
        return line, col

    def radioButtonChanged(self):
        print("value changed")
        print(self.stringVarRadioButton.get())

    def mapSelectedChanged(self, event):
        """
        Evenement déclanché lorsque l'utilisateur choisi une carte
        """

        # Nom de la carte sélectionnée
        self.mapName = self.comboBoxMapName.get()

        # object map associé
        self.map = mapManager.loadMapFileContent(self.mapName)
        self.labelRockAmount["text"] = f"Nombre de rocher {self.map.getRockAmount()}/{MAP_MAX_ROCK_AMOUNT}"

        self.drawGrid()
        #self.updateCanvasMap()

    def drawGrid(self):
        xStart = 10
        yStart = 10
        xPas = 22
        yPas = 22

        lineAmount = 20
        colAmount = 30

        lineSize = lineAmount * xPas
        colSize = colAmount * yPas

        
        for line in range(lineAmount):
            for col in range(colAmount):
                caseValue = self.map.getMatrix()[line][col]
                coords = (xStart + (col * xPas), yStart + (line * yPas))

                imgToDraw = None
                if (caseValue == 0):
                    imgToDraw = imageManager.IMG_MAP_AIR_TK
                elif (caseValue == 1):
                    imgToDraw = imageManager.IMG_MAP_ROCK_TK
                else:
                    print("Block id not found")

                super().drawImage(canvas=self.canvasMap, image=imgToDraw, posX=coords[0] + 10, posY=coords[1] + 10, tag=f"figure:{line},{col}")
            

        # Dessin des lignes
        for i in range(lineAmount + 1):
            self.canvasMap.create_line(xStart, yStart + (i * yPas), xStart + colSize, yStart + (i * yPas))

        # Dessin des colonnes
        for i in range(colAmount + 1):
            self.canvasMap.create_line(xStart + (i * xPas), yStart, xStart + (i * xPas), yStart + lineSize)