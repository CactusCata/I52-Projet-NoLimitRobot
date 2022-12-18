from random import randint

class Map:

    def __init__(self, matrixMap):
        self.matrixMap = matrixMap

        # Initialisation du nombre de rocher
        self.rockAmount = 0
        for line in self.matrixMap:
            for col in line:
                if col == 1:
                    self.rockAmount += 1

    def clear(self):
        """
        Remplie la map de vide
        """
        matrix = []
        for i in range(len(self.matrixMap)):
            matrix.append([0] * len(self.matrixMap[0]))

        self.matrixMap = matrix
        self.rockAmount = 0

    def isAccessible(self, pos):
        """
        Renvoie vrai si la case demandé est bien dans les dimensions de la map et que la case est accessible.
        Renvoie faux sinon
        """
        return 0 <= pos[0] < len(self.matrixMap) and 0 <= pos[1] < len(self.matrixMap[1]) and self.get(pos[0], pos[1]) == 0

    def getRockAmount(self):
        """
        Renvoie le nombre de rocher qu'il y a dans la map
        """
        return self.rockAmount

    def canPlaceAir(self, x, y):
        """
        Renvoie vrai si on peut placer un bloc d'air en (x,y)
        Sinon renvoie faux
        """
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
        """
        Place un bloc d'air si les conditions de canPlaceAir(x,y)
        sont respectées
        """
        if (self.get(x, y) == 0):
            return False

        if not self.canPlaceAir(x, y):
            return False

        self.rockAmount -= 1
        self.matrixMap[x][y] = 0
        return True

    def canPlaceRock(self, x, y):
        """
        Renvoie vrai si on peut placer un bloc de roche en (x,y)
        Sinon renvoie faux
        """
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
        """
        Place un bloc de roche si les conditions de canPlaceRock(x,y)
        sont respectées
        """
        if (self.get(x, y) == 1):
            return False

        if not self.canPlaceRock(x, y):
            return False


        self.rockAmount += 1
        self.matrixMap[x][y] = 1
        return True

    def placeTerreplein(self, x, y):
        """
        Place un terreplain en (x,y)
        """
        if (self.matrixMap[x][y] == 1):
            self.rockAmount -= 1

        self.matrixMap[x][y] = 2

    def getMatrix(self):
        """
        Renvoie la matrice correspondant à l'état
        de la map
        """
        return self.matrixMap

    def get(self, x, y):
        """
        Renvoie la valeur en (x,y) de la map
        """
        return self.matrixMap[x][y]

    def modify(self, x, y, type_obj):
        """
        Modifie une case de la carte afin de la mettre à jour.
        type_obj est le type de l'entité que l'on va mettre à jour sur la case.
        0 est pour l'air (case libre)
        1 est pour le rocher (case occupée)
        2 est pour les robots (case occupée)
        3 est pour les mines (case "libre" pour les déplacements, mais bloquante
        pour les projectiles)
        """
        self.matrixMap[x][y] = type_obj
