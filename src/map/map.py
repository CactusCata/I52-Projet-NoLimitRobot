import utils.mapUtils as mapUtils
import player.playerManager as playerManager

AIR_ID = 0
ROCK_ID = 1
PLAYER_ID = 2
MINE_ID = 3

class Map:
    """
    Carte/Arène du jeu
    Pour récuperer des infos sur la carte passer par les méthodes getID(x, y) et getData(x, y)
    Pour modifier des infos, utiliser la méthode modify(x, y, id, instance)
    """

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

        # Dimensions de la carte
        self.dimY = len(matrixMapBasic)
        self.dimX = len(matrixMapBasic[0])

        # Initialisation du nombre de rocher
        self.rockAmount = 0
        for i in range(self.dimY):
            lineMatrixID = []
            lineMatrixData = []
            for j in range(self.dimX):
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
        """
        Renvoie la largeur de la carte
        """
        return self.dimX

    def getDimY(self):
        """
        Renvoie la hauteur de la carte
        """
        return self.dimY

    def clear(self):
        """
        Remplie la map de bloc d'air
        """

        for x in range(self.dimX):
            for y in range(self.dimY):
                self.modify(x, y, AIR_ID, None)

        self.rockAmount = 0

    def removeData(self):
        """
        Supprime tous les robots et les mines de la carte
        """
        for x in range(self.dimX):
            for y in range(self.dimY):
                if self.getID(x, y) == MINE_ID or self.getID(x, y) == PLAYER_ID:
                    self.modify(x, y, AIR_ID, None)

    def isAccessible(self, pos):
        """
        Renvoie vrai si la case demandé est bien dans les dimensions de la map et que la case est accessible.
        Renvoie faux sinon
        """
        return 0 <= pos[0] < self.dimX and 0 <= pos[1] < self.dimY and (self.getID(pos[0], pos[1]) == AIR_ID or self.getID(pos[0], pos[1]) == MINE_ID)

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
        if (y > 0 and x < 29):
            if self.getID(x, y - 1) == ROCK_ID and self.getID(x + 1, y) == ROCK_ID and self.getID(x + 1, y - 1) == AIR_ID:
                return False

        # Coin supérieur gauche
        if (y < 19 and x < 29):
            if self.getID(x + 1, y) == ROCK_ID and self.getID(x, y + 1) == ROCK_ID and self.getID(x + 1, y + 1) == AIR_ID:
                return False

        # Coin supérieur droit
        if (y < 19 and x > 0):
            if self.getID(x - 1, y) == ROCK_ID and self.getID(x, y + 1) == ROCK_ID and self.getID(x - 1, y + 1) == AIR_ID:
                return False

        # Coin inférieur droit
        if (y > 0 and x > 0):
            if self.getID(x - 1, y) == ROCK_ID and self.getID(x, y - 1) == ROCK_ID and self.getID(x - 1, y - 1) == AIR_ID:
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
        self.modify(x, y, AIR_ID, None)
        return True

    def canPlaceRock(self, x, y):
        """
        Renvoie vrai si on peut placer un bloc de roche en (x,y)
        Sinon renvoie faux
        """
        # Coin inférieur gauche
        if (y > 0 and x < 29):
            if self.getID(x + 1, y) == AIR_ID and self.getID(x, y - 1) == AIR_ID and self.getID(x + 1, y - 1) == ROCK_ID:
                return False

        # Coin supérieur gauche
        if (y < 19 and x < 29):
            if self.getID(x + 1, y) == AIR_ID and self.getID(x, y + 1) == AIR_ID and self.getID(x + 1, y + 1) == ROCK_ID:
                return False

        # Coin supérieur droit
        if (y < 19 and x > 0):
            if self.getID(x - 1, y) == AIR_ID and self.getID(x, y + 1) == AIR_ID and self.getID(x - 1, y + 1) == ROCK_ID:
                return False

        # Coin inférieur droit
        if (y > 0 and x > 0):
            if self.getID(x - 1, y) == AIR_ID and self.getID(x, y - 1) == AIR_ID and self.getID(x - 1, y - 1) == ROCK_ID:
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
        self.modify(x, y, ROCK_ID, None)
        return True

    def serializeMatrixID(self):
        """
        Return the matrix of ids.
        Do not use this function if you want to travel
        with (x, y) coords, only for serialization.
        """
        return self.matrixMapID

    def getID(self, x, y):
        """
        Renvoie l'ID en (x,y) de la map
        """
        return self.matrixMapID[y][x]

    def getData(self, x, y):
        """
        Renvoie l'instance de l'objet en (x,y) de la map
        """
        return self.matrixMapInstance[y][x]

    def modify(self, x, y, id_object, object):
        """
        Modifie une case de la carte afin de la mettre à jour.
        type_obj est le type de l'entité que l'on va mettre à jour sur la case.
        0 est pour l'air (case libre)
        1 est pour le rocher (case occupée)
        2 est pour les robots (case occupée)
        3 est pour les mines (case "libre" pour les déplacements, mais bloquante
        pour les projectiles)
        """
        self.matrixMapID[y][x] = id_object
        self.matrixMapInstance[y][x] = object


    def getNearestRobot(self, robot):
        """
        Renvoie un couple:
        - instance de robot qui se trouve être le plus proche
        - le path de notre robot jusqu'au robot le plus proche
        Renvoie le couple (None, None) si aucun robot n'est accessible (joueur seul ou les autres sont en vanish)
        """
        startX = robot.get_x()
        startY = robot.get_y()

        # Récupère le robot le plus proche
        i = 0
        nearestRobot = None
        nearestRobotPath = None
        while i < len(playerManager.PLAYER_LIST) and nearestRobot is None:
            playerRobot = playerManager.PLAYER_LIST[i].getRobotParty()
            if playerRobot != robot and not playerRobot.is_vanish() and playerRobot.get_energy() > 0:
                nearestRobot = playerRobot
                nearestRobotPath = mapUtils.getPath(self, (startX, startY), (playerRobot.get_x(), playerRobot.get_y()))
            i += 1


        for player in playerManager.PLAYER_LIST:
            playerRobot = player.getRobotParty()
            if (playerRobot != robot and not playerRobot.is_vanish() and playerRobot.get_energy() > 0):
                currentPath = mapUtils.getPath(self, (startX, startY), (playerRobot.get_x(), playerRobot.get_y()))
                if (len(currentPath) < len(nearestRobotPath)):
                    nearestRobot = playerRobot
                    nearestRobotPath = currentPath

        return (nearestRobot, nearestRobotPath)

    def placeMine(self, mine):
        """
        Place une mine à la position attendue
        """
        x = mine.get_x()
        y = mine.get_y()
        self.modify(x, y, MINE_ID, mine)

    def robotShoot(self, robot, selectedDirection, damage):
        """
        Tire dans la direction Nord (N), Sud (S), Est (E), Ouest (O).
        Si un robot est sur le chemin, alors on applique le dégats.
        Si un mur est sur le chemin, le mur bloque la balle.
        La balle passe à travers l'air et les mines.
        """
        x = robot.get_x()
        y = robot.get_y()

        playerID = 0
        for i in range(len(playerManager.PLAYER_LIST)):
            player = playerManager.PLAYER_LIST[i]
            if player.getRobotParty() == robot:
                playerID = i
                break

        directionVect = [0, 0]
        if selectedDirection == "H":
            directionVect[1] += -1
        elif selectedDirection == "B":
            directionVect[1] += 1
        elif selectedDirection == "D":
            directionVect[0] += 1
        elif selectedDirection == "G":
            directionVect[0] += -1
        else:
            print(f"map.robotShoot(...): direction \"{selectedDirection}\" is unknowed")

        # On continue tant qu'on est pas sortie
        # des dimensions de la carte
        # ou qu'on a pas croisé un obstacle
        x += directionVect[0]
        y += directionVect[1]
        while (1 < x < self.getDimX() - 2) and (1 < y < self.getDimY() - 2) and (self.getID(x, y) == AIR_ID or self.getID(x, y) == MINE_ID):
            if (self.getID(x, y) == MINE_ID):
                mine = self.getData(x, y)
                if mine.get_playerId() != playerID:
                    self.modify(x, y, AIR_ID, None)
            x += directionVect[0]
            y += directionVect[1]

        # Si l'obstacle est une joueur, lui appliquer les dégats
        if self.isAccessible((x, y)) and self.getID(x, y) == PLAYER_ID:
            robot = self.getData(x, y)
            robot.decreaseEnery(damage)

    def updateRobotPosition(self, robot, position):
        """
        Permet de mettre à jour la position d'un robotParty sur la carte.
        Si une mine est présente sur la position du déplacement, alors
        elle explose causant des dégats au robot et active l'instruction
        de danger pour le robot
        """

        playerID = 0
        for i in range(len(playerManager.PLAYER_LIST)):
            player = playerManager.PLAYER_LIST[i]
            if player.getRobotParty() == robot:
                playerID = i
                break
        playerMoved = playerManager.PLAYER_LIST[playerID]

        # Si le robot qui se déplace tombe sur une mine,
        # Alors lui infliger des dégats
        x = position[0]
        y = position[1]
        if self.getID(x, y) == MINE_ID:
            mine = self.getData(x, y)
            playerHasPutThisMineID = mine.get_playerId()
            playerHasPutThisMine = playerManager.PLAYER_LIST[playerHasPutThisMineID]
            if (playerHasPutThisMine.getRobotParty() != robot):
                robot.decreaseEnery(mine.get_damage())
                playerMoved.enable_danger_instruction()

        self.modify(robot.get_x(), robot.get_y(), AIR_ID, None)
        robot.move(position)
        
        self.modify(x, y, PLAYER_ID, robot)

    def copyMapID(self):
        """
        Renvoie une copie de la matrice des id
        """
        matrix = []
        for i in range(self.dimX):
            line = []
            for j in range(self.dimY):
                line.append(self.getID(i, j))
            matrix.append(line)
        return matrix

    def copyMapInstance(self):
        """
        Renvoie une copie de la matrice des instances
        """
        matrix = []
        for i in range(self.dimX):
            line = []
            for j in range(self.dimY):
                res = self.getData(i, j)
                if (res == None):
                    line.append(None)
                else:
                    line.append(res.copy())
            matrix.append(line)
        return matrix