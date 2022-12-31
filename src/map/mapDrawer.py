from map.mapManager import MAP_LINE_AMOUNT, MAP_COL_AMOUNT

import image.imageManager as imageManager
import utils.tkinter.tkUtils as tkUtils

class MapDrawer:

    def __init__(self, canvas, map, players=[], xStart=10, yStart=10, xPas=22, yPas=22):
        self.canvas = canvas
        self.map = map
        self.players = players

        self.xStart = xStart
        self.yStart = yStart
        self.xPas = xPas
        self.yPas = yPas

        self.robotsDrawID = []

    def drawGrid(self):
        lineSize = self.map.getDimY() * self.xPas
        colSize = self.map.getDimX() * self.yPas

        # Dessin des lignes
        for i in range(self.map.getDimY() + 1):
            self.canvas.create_line(self.xStart, self.yStart + (i * self.yPas), self.xStart + colSize, self.yStart + (i * self.yPas))

        # Dessin des colonnes
        for i in range(self.map.getDimX() + 1):
            self.canvas.create_line(self.xStart + (i * self.xPas), self.yStart, self.xStart + (i * self.xPas), self.yStart + lineSize)

    def drawMap(self):
        for x in range(self.map.getDimX()):
            for y in range(self.map.getDimY()):
                caseValue = self.map.getID(x, y)
                #coords = (self.xStart + (col * self.xPas), self.yStart + (line * self.yPas))

                imgToDraw = None
                if (caseValue == 1):
                    imgToDraw = imageManager.IMG_MAP_ROCK_TK
                else:
                    imgToDraw = imageManager.IMG_MAP_AIR_TK

                if (imgToDraw != None):
                    self.drawImage(imgToDraw, x, y, tag=f"figure:{x},{y}")
                #self.canvas.create_image(coords[0] + 10, coords[1] + 10, image=imgToDraw, tag=(f"figure:{line},{col}",))
               
    def drawRobot(self):
        for player in self.players:
            robotParty = player.getRobotParty()
            self.drawImage(player.getRobotBlocTk(), robotParty.get_x(), robotParty.get_y())


    def drawImage(self, img, col, line, tag=""):
        return self.canvas.create_image(col*self.xPas + (self.xPas - 1), line*self.yPas + (self.yPas - 1), image=img, tag=(tag,))

    def getItemCoordinates(self, itemID):
        tag = tkUtils.itemHasTag(self.canvas, itemID, tkUtils.startWithFunction, "figure")

        if (tag == None):
            return None

        coordsInfo = tag.split(":")[1]
        x = int(coordsInfo.split(",")[0])
        y = int(coordsInfo.split(",")[1])
        return (x, y)

    def clear(self):
        self.canvas.delete("all")