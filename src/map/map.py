class Map:

    def __init__(self, matrixMap):
        self.matrixMap = matrixMap

    def placeAir(self, x, y):
        self.matrixMap[x][y] = 0

    def placeRock(self, x, y):
        self.matrixMap[x][y] = 1

    def placeTerreplein(self, x, y):
        self.matrixMap[x][y] = 2

    def getMatrix(self):
        return self.matrixMap