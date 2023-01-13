import math
import player.playerManager as playerManager

class RobotChooser:
    """
    Classe qui permet le choix des robots
    """

    def __init__(self, canvas, robotsFileList=[], xStart=10, yStart=10):

        # Canvas où on dessine les robots
        self.canvas = canvas

        # Liste des robots à dessiner
        self.robotsFileList = robotsFileList

        # dictionnaire des img des images
        self.dictIdRobotFile = {}

        # Début du dessin des robots
        self.xStart = xStart
        self.yStart = yStart

        # Pas en pixel entre chaque case
        self.xPas = playerManager.PLAYER_ICON_DIMENSIONS[0] + 2
        self.yPas = playerManager.PLAYER_ICON_DIMENSIONS[1] + 2

        # Dimensions (n * n) de la matrice de choix des robots
        self.matrixDim = math.ceil(math.sqrt(len(robotsFileList)))

    def drawGrid(self):
        """
        Dessine une grille
        """
        lineSize = self.matrixDim * self.xPas
        colSize = self.matrixDim * self.yPas

        # Dessin des lignes
        for i in range(self.matrixDim + 1):
            self.canvas.create_line(self.xStart, self.yStart + (i * self.yPas), self.xStart + colSize, self.yStart + (i * self.yPas))

        # Dessin des colonnes
        for i in range(self.matrixDim + 1):
            self.canvas.create_line(self.xStart + (i * self.xPas), self.yStart, self.xStart + (i * self.xPas), self.yStart + lineSize)

    def drawRobots(self):
        """
        Dessine les robots
        """
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
        """
        Dessine une image
        """
        return self.canvas.create_image(playerManager.PLAYER_ICON_DIMENSIONS[0] // 2 + self.xStart + col * self.xPas, playerManager.PLAYER_ICON_DIMENSIONS[1] // 2 + self.yStart + line * self.yPas, image=img, tag=(tag,))

    def getRobotFile(self, id):
        return self.dictIdRobotFile[id]