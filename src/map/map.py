class Map:

    def __init__(self, matrixMapBasic):

        # La matrice d'ID contient les id:
        # air: 0
        # rocher: 1
        # joueur: 2
        # mine: 3
        self.matrixMapID = []

        # La matrice d'instance contient les instances des objets
        # manipulés si elles en sont:
        # air: None
        # rocher: None
        # joueur: instance de RobotParty
        # mine: instance de Mine
        self.matrixMapInstance = []

        self.dimX = len(matrixMapBasic)
        self.dimY = len(matrixMapBasic[0])

        # Initialisation du nombre de rocher
        self.rockAmount = 0
        for i in range(self.dimX):
            lineMatrixID = []
            lineMatrixData = []
            for j in range(self.dimY):
                if matrixMapBasic[i][j] == 1:
                    self.rockAmount += 1
                    lineMatrixID.append(1)
                    lineMatrixData.append(None)
                elif matrixMapBasic[i][j] == 0:
                    lineMatrixID.append(0)
                    lineMatrixData.append(None)
            self.matrixMapID.append(lineMatrixID)
            self.matrixMapInstance.append(lineMatrixData)

    def getDimX(self):
        return self.dimX

    def getDimY(self):
        return self.dimY

    def clear(self):
        """
        Remplie la map de vide
        """

        for i in range(self.dimX):
            for j in range(self.dimY):
                self.matrixMapID[i][j] = 0
                self.matrixMapInstance[i][j] = None

        self.rockAmount = 0

    def isAccessible(self, pos):
        """
        Renvoie vrai si la case demandé est bien dans les dimensions de la map et que la case est accessible.
        Renvoie faux sinon
        """
        return 0 <= pos[0] < self.dimX and 0 <= pos[1] < self.dimY and self.getID(pos[0], pos[1]) == 0

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
            if self.getID(x - 1, y + 1) == 0 and self.getID(x - 1, y) == 1 and self.getID(x, y + 1) == 1:
                return False

        # Coin supérieur gauche
        if (x > 0 and y > 0):
            if self.getID(x - 1, y - 1) == 0 and self.getID(x - 1, y) == 1 and self.getID(x, y - 1) == 1:
                return False

        # Coin supérieur droit
        if (x < 19 and y > 0):
            if self.getID(x + 1, y - 1) == 0 and self.getID(x + 1, y) == 1 and self.getID(x, y - 1) == 1:
                return False

        # Coin inférieur droit
        if (x < 19 and y < 29):
            if self.getID(x + 1, y + 1) == 0 and self.getID(x + 1, y) == 1 and self.getID(x, y + 1) == 1:
                return False

        return True

    def placeAir(self, x, y):
        """
        Place un bloc d'air si les conditions de canPlaceAir(x,y)
        sont respectées
        """
        if (self.getID(x, y) == 0):
            return False

        if not self.canPlaceAir(x, y):
            return False

        self.rockAmount -= 1
        self.matrixMapID[x][y] = 0
        self.matrixMapInstance[x][y] = None
        return True

    def canPlaceRock(self, x, y):
        """
        Renvoie vrai si on peut placer un bloc de roche en (x,y)
        Sinon renvoie faux
        """
        # Coin inférieur gauche
        if (x > 0 and y < 29):
            if self.getID(x - 1, y + 1) == 1 and self.getID(x - 1, y) == 0 and self.getID(x, y + 1) == 0:
                return False

        # Coin supérieur gauche
        if (x > 0 and y > 0):
            if self.getID(x - 1, y - 1) == 1 and self.getID(x - 1, y) == 0 and self.getID(x, y - 1) == 0:
                return False

        # Coin supérieur droit
        if (x < 19 and y > 0):
            if self.getID(x + 1, y - 1) == 1 and self.getID(x + 1, y) == 0 and self.getID(x, y - 1) == 0:
                return False

        # Coin inférieur droit
        if (x < 19 and y < 29):
            if self.getID(x + 1, y + 1) == 1 and self.getID(x + 1, y) == 0 and self.getID(x, y + 1) == 0:
                return False

        return True

    def placeRock(self, x, y):
        """
        Place un bloc de roche si les conditions de canPlaceRock(x,y)
        sont respectées
        """
        if (self.getID(x, y) == 1):
            return False

        if not self.canPlaceRock(x, y):
            return False


        self.rockAmount += 1
        self.matrixMapID[x][y] = 1
        self.matrixMapInstance[x][y] = None
        return True

    def getMatrix(self):
        """
        Renvoie la matrice correspondant à l'état
        de la map
        """
        return self.matrixMapID

    def getID(self, x, y):
        """
        Renvoie l'ID en (x,y) de la map
        """
        return self.matrixMapID[x][y]

    def getData(self, x, y):
        """
        Renvoie l'instance de l'objet en (x,y) de la map
        """
        return self.matrixMapInstance[x][y]

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
        self.matrixMapID[x][y] = type_obj
