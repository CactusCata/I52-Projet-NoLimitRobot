import player.playerManager as playerManager

import image.imageManager as imageManager
import utils.tkinter.tkUtils as tkUtils

class MapDrawer:

    def __init__(self, canvas, map, players=[], xStart=10, yStart=10):
        self.canvas = canvas
        self.map = map
        self.players = players

        self.xStart = xStart
        self.yStart = yStart
        self.xPas = imageManager.MAP_BLOC_DIMENSIONS[0] + 2
        self.yPas = imageManager.MAP_BLOC_DIMENSIONS[1] + 2

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

                imgToDraw = None
                if (caseValue == 1):
                    imgToDraw = imageManager.IMG_MAP_ROCK_TK
                else:
                    imgToDraw = imageManager.IMG_MAP_AIR_TK

                if (imgToDraw != None):
                    self.drawImage(imgToDraw, x, y, tag=f"figure:{x},{y}")

    def drawRobot(self):
        for player in self.players:
            robotParty = player.getRobotParty()
            self.drawImage(player.getRobotBlocTk(), robotParty.get_x(), robotParty.get_y())

    def drawMine(self):
        for x in range(self.map.getDimX()):
            for y in range(self.map.getDimY()):
                if (self.map.getID(x, y) == 3):
                    mine = self.map.getData(x, y)
                    playerID = mine.get_playerId()
                    player = playerManager.PLAYER_LIST[playerID]
                    mineBlockTk = player.getMineBlocTk()
                    self.drawImage(mineBlockTk, x, y)


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