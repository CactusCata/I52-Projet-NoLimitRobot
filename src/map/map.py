from random import randint

class Map:

    def __init__(self, matrixMap):
        self.matrixMap = matrixMap

        self.rockAmount = 0
        for line in self.matrixMap:
            for col in line:
                if col == 1:
                    self.rockAmount += 1

    def clear(self):
        matrix = []
        for i in range(len(self.matrixMap)):
            matrix.append([0] * len(self.matrixMap[0]))

        self.matrixMap = matrix
        self.rockAmount = 0

    def getRockAmount(self):
        return self.rockAmount

    def canPlaceAir(self, x, y):
        # Coin inférieur gauche
        if (x > 0 and y < 29):
            if self.get(x - 1, y + 1) == 0 and self.get(x - 1, y) == 1 and self.get(x, y + 1) == 1:
                return False
        
        # Coin supérieur gauche
        if (x > 0 and y > 0):
            if self.get(x - 1, y - 1) == 0 and self.get(x - 1, y) == 1 and self.get(x, y - 1) == 1:
                return False

        # Coin supérieur droit
        if (x < 19 and y > 0):
            if self.get(x + 1, y - 1) == 0 and self.get(x + 1, y) == 1 and self.get(x, y - 1) == 1:
                return False

        # Coin inférieur droit
        if (x < 19 and y < 29):
            if self.get(x + 1, y + 1) == 0 and self.get(x + 1, y) == 1 and self.get(x, y + 1) == 1:
                return False

        return True

    def placeAir(self, x, y):
        if (self.get(x, y) == 0):
            return False

        if not self.canPlaceAir(x, y):
            return False

        self.rockAmount -= 1
        self.matrixMap[x][y] = 0
        return True

    def canPlaceRock(self, x, y):
        # Coin inférieur gauche
        if (x > 0 and y < 29):
            if self.get(x - 1, y + 1) == 1 and self.get(x - 1, y) == 0 and self.get(x, y + 1) == 0:
                return False
        
        # Coin supérieur gauche
        if (x > 0 and y > 0):
            if self.get(x - 1, y - 1) == 1 and self.get(x - 1, y) == 0 and self.get(x, y - 1) == 0:
                return False

        # Coin supérieur droit
        if (x < 19 and y > 0):
            if self.get(x + 1, y - 1) == 1 and self.get(x + 1, y) == 0 and self.get(x, y - 1) == 0:
                return False

        # Coin inférieur droit
        if (x < 19 and y < 29):
            if self.get(x + 1, y + 1) == 1 and self.get(x + 1, y) == 0 and self.get(x, y + 1) == 0:
                return False

        return True

    def placeRock(self, x, y):
        if (self.get(x, y) == 1):
            return False

        if not self.canPlaceRock(x, y):
            return False

               
        self.rockAmount += 1
        self.matrixMap[x][y] = 1
        return True

    def placeTerreplein(self, x, y):
        if (self.matrixMap[x][y] == 1):
            self.rockAmount -= 1

        self.matrixMap[x][y] = 2

    def getMatrix(self):
        return self.matrixMap

    def get(self, x, y):
        return self.matrixMap[x][y]

    def isLegal(self):
        mapLineAmount = len(self.matrixMap)
        mapColAmount = len(self.matrixMap[i])
        for i in range(mapLineAmount - 1):
            for j in range(mapColAmount - 1):
                if (self.matrixMap[i][j] == 0 and self.matrixMap[i][j + 1] == 1 and self.matrixMap[i + 1][j] == 1 and self.matrixMap[i + 1][j + 1] == 0):
                    return False
                if (self.matrixMap[i][j] == 1 and self.matrixMap[i][j + 1] == 0 and self.matrixMap[i + 1][j] == 0 and self.matrixMap[i + 1][j + 1] == 1):
                    return False

    def suffle(self):
        lineAmount = len(self.matrixMap)
        colAmount = len(self.matrixMap[0])
        n = lineAmount * colAmount
        for i in range(n):
            foundPlace = False
            while not foundPlace:
                j = i + randint(1 << 13) % ((n - 1) - i + 1)
                leftLine = n // i
                leftCol = i % lineAmount
                rightLine = n // j
                rightCol = j % lineAmount


