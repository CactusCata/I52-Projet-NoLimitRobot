import math

class RobotChoosen:

    def __init__(self, canvas, robotsFileList=[], xStart=10, yStart=10, xPas=22, yPas=22):
        self.canvas = canvas
        self.robotsFileList = robotsFileList

        self.xStart = xStart
        self.yStart = yStart
        self.xPas = xPas
        self.yPas = yPas

        self.matrixDim = math.floor(math.sqrt(len(robotsFileList)))

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
                imgToDraw = robotFile.getLogo()

                self.drawImage(imgToDraw, line, col, tag=f"robot:{line * self.matrixDim + col}")
                

    def drawImage(self, img, line, col, tag=""):
        self.canvas.create_image(col*self.xPas + (self.xPas - 1), line*self.yPas + (self.yPas - 1), image=img, tag=(tag,))
