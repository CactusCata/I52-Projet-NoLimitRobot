import math
import player.playerManager as playerManager

class RobotChooser:

    def __init__(self, canvas, robotsFileList=[], xStart=10, yStart=10):
        self.canvas = canvas
        self.robotsFileList = robotsFileList
        self.dictIdRobotFile = {}

        self.xStart = xStart
        self.yStart = yStart
        self.xPas = playerManager.PLAYER_ICON_DIMENSIONS[0] + 2
        self.yPas = playerManager.PLAYER_ICON_DIMENSIONS[1] + 2

        self.matrixDim = math.ceil(math.sqrt(len(robotsFileList)))

    def drawGrid(self):
        lineSize = self.matrixDim * self.xPas
        colSize = self.matrixDim * self.yPas

        # Dessin des lignes
        for i in range(self.matrixDim + 1):
            self.canvas.create_line(self.xStart, self.yStart + (i * self.yPas), self.xStart + colSize, self.yStart + (i * self.yPas))

        # Dessin des colonnes
        for i in range(self.matrixDim + 1):
            self.canvas.create_line(self.xStart + (i * self.xPas), self.yStart, self.xStart + (i * self.xPas), self.yStart + lineSize)

    def drawRobots(self):
        line = 0
        while (line < self.matrixDim) and (line * self.matrixDim < len(self.robotsFileList)):
            col = 0
            while (col < self.matrixDim) and (line * self.matrixDim + col < len(self.robotsFileList)):
                robotFile = self.robotsFileList[line * self.matrixDim + col]
                robotFile.load_icon()
                robotFile.load_icon_tk()
                imgToDraw = robotFile.get_icon_tk()

                id = self.drawImage(imgToDraw, line, col, tag=f"robot:{line * self.matrixDim + col}")
                self.dictIdRobotFile[id] = robotFile
                col += 1

            line += 1
                

    def drawImage(self, img, line, col, tag=""):
        # Juste
        return self.canvas.create_image(playerManager.PLAYER_ICON_DIMENSIONS[0] // 2 + self.xStart + col * self.xPas, playerManager.PLAYER_ICON_DIMENSIONS[1] // 2 + self.yStart + line * self.yPas, image=img, tag=(tag,))

    def getRobotFile(self, id):
        return self.dictIdRobotFile[id]