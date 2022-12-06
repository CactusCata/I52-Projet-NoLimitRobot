import frame.rootManager as rootManager
import map.mapManager as mapManager
import image.imageManager as imageManager

from frame.iFrame import IFrame

class FEditMap(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

        self.placeBlockType = 0

    def draw(self):
        root = rootManager.getRoot()

        labelMapName = super().createLabel(text="Choisir la map:")
        labelMapName.pack()

        self.comboBoxMapName = super().createComboBox(list=mapManager.getLoadedMaps(), callback=lambda event: self.mapSelectedChanged(event))
        self.comboBoxMapName.pack()

        self.canvasMap = super().createCanvas(width=700, height=500)
        self.canvasMap.pack()

    def mapSelectedChanged(self, event):
        """
        Evenement déclanché lorsque l'utilisateur choisi une carte
        """

        # Nom de la carte sélectionnée
        mapName = self.comboBoxMapName.get()

        # object map associé
        map = mapManager.loadMapFileContent(mapName)
        print(map)

        self.drawGrid(map)

    def drawGrid(self, map):
        xStart = 10
        yStart = 10
        xPas = 20
        yPas = 20

        lineAmount = 20
        colAmount = 30

        lineSize = lineAmount * xPas
        colSize = colAmount * yPas

        
        for line in range(lineAmount):
            for col in range(colAmount):
                caseValue = map.getMatrix()[line][col]
                coords = (xStart + (col * xPas), yStart + (line * yPas))
                print(coords)

                imgToDraw = None
                if (caseValue == 0):
                    imgToDraw = imageManager.IMG_MAP_AIR_TK
                elif (caseValue == 1):
                    imgToDraw = imageManager.IMG_MAP_ROCK_TK
                else:
                    print("Block id not found")

                super().drawImage(canvas=self.canvasMap, image=imgToDraw, posX=coords[0] + 10, posY=coords[1] + 10)
            

        # Dessin des lignes
        for i in range(lineAmount + 1):
            self.canvasMap.create_line(xStart, yStart + (i * yPas), xStart + colSize, yStart + (i * yPas))

        # Dessin des colonnes
        for i in range(colAmount + 1):
            self.canvasMap.create_line(xStart + (i * xPas), yStart, xStart + (i * xPas), yStart + lineSize)