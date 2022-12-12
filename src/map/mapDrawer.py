from map.mapManager import MAP_LINE_AMOUNT, MAP_COL_AMOUNT

import image.imageManager as imageManager
import utils.tkUtils as tkUtils

class MapDrawer:

    def __init__(self, canvas, map, robots=[], xStart=10, yStart=10, xPas=22, yPas=22):
        self.canvas = canvas
        self.map = map
        self.robots = robots

        self.xStart = xStart
        self.yStart = yStart
        self.xPas = xPas
        self.yPas = yPas

    def drawGrid(self):
        lineSize = MAP_LINE_AMOUNT * self.xPas
        colSize = MAP_COL_AMOUNT * self.yPas

        # Dessin des lignes
        for i in range(MAP_LINE_AMOUNT + 1):
            self.canvas.create_line(self.xStart, self.yStart + (i * self.yPas), self.xStart + colSize, self.yStart + (i * self.yPas))

        # Dessin des colonnes
        for i in range(MAP_COL_AMOUNT + 1):
            self.canvas.create_line(self.xStart + (i * self.xPas), self.yStart, self.xStart + (i * self.xPas), self.yStart + lineSize)

    def drawMap(self):
        for line in range(MAP_LINE_AMOUNT):
            for col in range(MAP_COL_AMOUNT):
                caseValue = self.map.getMatrix()[line][col]
                #coords = (self.xStart + (col * self.xPas), self.yStart + (line * self.yPas))

                imgToDraw = None
                if (caseValue == 0):
                    imgToDraw = imageManager.IMG_MAP_AIR_TK
                elif (caseValue == 1):
                    imgToDraw = imageManager.IMG_MAP_ROCK_TK
                else:
                    print("Block id not found")

                self.drawImage(imgToDraw, line, col, tag=f"figure:{line},{col}")
                #self.canvas.create_image(coords[0] + 10, coords[1] + 10, image=imgToDraw, tag=(f"figure:{line},{col}",))
               
    def drawRobot(self):
        pass

    def drawImage(self, img, line, col, tag=""):
        self.canvas.create_image(col*self.xPas + (self.xPas - 1), line*self.yPas + (self.yPas - 1), image=img, tag=(tag,))

    def getItemCoordinates(self, itemID):
        tag = tkUtils.itemHasTag(self.canvas, itemID, tkUtils.startWithFunction, "figure")

        if (tag == None):
            return None

        coordsInfo = tag.split(":")[1]
        line = int(coordsInfo.split(",")[0])
        col = int(coordsInfo.split(",")[1])
        return (line, col)

    def clear(self):
        self.canvas.delete("all")