import player.playerManager as playerManager

import image.imageManager as imageManager
import utils.tkinter.tkUtils as tkUtils

import random

MS_BETWEEN_TWO_IP_REFRESH = 20

class MapDrawer:

    def __init__(self, canvas, map, players=[], xStart=10, yStart=10):
        self.canvas = canvas
        self.map = map
        self.players = players

        self.xStart = xStart
        self.yStart = yStart
        self.xPas = imageManager.MAP_BLOC_DIMENSIONS[0] + 2
        self.yPas = imageManager.MAP_BLOC_DIMENSIONS[1] + 2

        self.ipNumber = 0
        self.ipMvmt = +1
        self.ipTaskID = -1
        self.lastActiveID = -1
        self.lastIPImgIDs = []

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


    def startDrawIPs(self, robotsPosition):
        self.lastActiveID = random.randint(0, 1 << 12)
        self.drawIps(robotsPosition, self.lastActiveID)

    def drawIps(self, robotsPosition, lastActiveID):
        for imgID in self.lastIPImgIDs:
            self.canvas.delete(imgID)

        if (self.lastActiveID != lastActiveID):
            return

        for robotPosition in robotsPosition:
            imgID = self.drawImage(imageManager.IMG_MAP_INTERROGATIVE_POINT_TRANSPARENT_TK[self.ipNumber], robotPosition[0], robotPosition[1])
            self.lastIPImgIDs.append(imgID)

        self.ipNumber += self.ipMvmt
        if self.ipNumber == imageManager.IMG_MAP_INTERROGATIVE_POINT_TRANSPARENT_AMOUNT:
            self.ipNumber -= 1
            self.ipMvmt = -1
        elif self.ipNumber == -1:
            self.ipNumber += 1
            self.ipMvmt = +1

        self.ipTaskID = self.canvas.after(MS_BETWEEN_TWO_IP_REFRESH, lambda: self.drawIps(robotsPosition, lastActiveID))

    def stopDrawIPs(self):
        self.lastActiveID = random.randint(0, 1 << 12)

    def startDrawBigIP(self):
        self.lastActiveID = random.randint(0, 1 << 12)
        self.drawBigIP(self.lastActiveID)

    def drawBigIP(self, lastActiveID):
        for imgID in self.lastIPImgIDs:
            self.canvas.delete(imgID)

        if (lastActiveID != self.lastActiveID):
            return

        imgID = self.drawImage(imageManager.IMG_MAP_INTERROGATIVE_BIG_POINT_TRANSPARENT_TK[self.ipNumber], 10, 7)
        self.lastIPImgIDs.append(imgID)

        self.ipNumber += self.ipMvmt
        if self.ipNumber == imageManager.IMG_MAP_INTERROGATIVE_POINT_TRANSPARENT_AMOUNT:
            self.ipNumber -= 1
            self.ipMvmt = -1
        elif self.ipNumber == -1:
            self.ipNumber += 1
            self.ipMvmt = +1

        self.ipTaskID = self.canvas.after(MS_BETWEEN_TWO_IP_REFRESH, lambda: self.drawBigIP(lastActiveID))


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