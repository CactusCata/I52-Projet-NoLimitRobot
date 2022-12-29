import math
import random

import utils.mathsUtils as mathsUtils

def getRandomValideRobotPosition(map):
    """
    Renvoie une position aléatoire valide sur la map
    """
    position = (random.randint(0, map.getDimX() - 1), random.randint(0, map.getDimY() - 1))
    while (not map.isAccessible(position[0], position[1])):
        position = (random.randint(0, map.getDimX() - 1), random.randint(0, map.getDimY() - 1))

    return position

def getMinDistanceBetweenRobotAndOthers(map, robotPosition, robotsPosition):
    """
    Renvoie la plus petite distance entre un robot
    """
    minDistance = mathsUtils.distance(robotPosition[0], robotPosition[1], robotsPosition[0][0], robotsPosition[0][1])
    for i in range(1, len(robotsPosition)):
        currentDistance = mathsUtils.distance(robotPosition[0], robotPosition[1], robotsPosition[i][0], robotsPosition[i][1])
        if minDistance > currentDistance:
            minDistance = currentDistance

    return minDistance

def generateRandomSpreadRobotPositions(map, playerAmount, minDistance, maxTried=10):
    """
    Génère un ensemble de position aléatoire pour les robots avec une distance minimale à
    respecter entre chaque robot
    """
    robotsPosition = []

    for i in range(playerAmount):
        tryedCount = 0
        randomPosition = getRandomValideRobotPosition(map)
        currentMinDistance = getMinDistanceBetweenRobotAndOthers(randomPosition)
        while (currentMinDistance > minDistance and tryedCount < maxTried):
            randomPosition = getRandomValideRobotPosition(map)
            currentMinDistance = getMinDistanceBetweenRobotAndOthers(randomPosition)
            tryedCount += 1
        robotsPosition.append(randomPosition)

    return robotsPosition


def generateEquidistanceRobotsPositions(map, playerAmount):
    """
    Génère des positions en forme de cercle sur la map
    pour répartir les robots.
    Les positionnes à des endroits où la case est accessible.
    """
    print("Appel de generateEquidistanceRobotsPositions(...)")

    robotsPositions = []
    mapDimX = map.getDimX()
    mapDimY = map.getDimY()

    for i in range(playerAmount):
        alpha = (2 * math.pi * i) / playerAmount
        robotPosition = (int((1 + math.cos(alpha)) * mapDimX * 0.4), int((1 + math.sin(alpha)) * mapDimY * 0.4))
        print(f"robot number {i}")
        robotPosition = generateValideRobotPosition(map, robotPosition)
        robotsPositions.append(robotPosition)

    print(f"generateEquidistanceRobotsPositions(...): {robotPosition}")
    return robotsPositions

def generateValideRobotPosition(map, robotPosition):
    """
    Génère une position valide autour d'un point pour le robot
    dont la position est robotPosition.
    """
    validposition = None
    j = 0
    while validposition is None:
        possiblesPositions = generateSquarePositions(j)
        random.shuffle(possiblesPositions)

        k = 0
        while k < len(possiblesPositions) and validposition is None:
            currentSelectedPosition = possiblesPositions[k]

            print(f"robotPosition = {robotPosition} | currentSelectedPosition = {currentSelectedPosition}")

            # Si la case est accessible, on arrête la recherche de case valide
            if map.isAccessible((robotPosition[0] + currentSelectedPosition[0], robotPosition[1] + currentSelectedPosition[1])):
                validposition = ((robotPosition[0] + currentSelectedPosition[0], robotPosition[1] + currentSelectedPosition[1]))
            
            k += 1
        
        j += 1

    return validposition


def generateSquarePositions(n):
    """
    Génère l'ensemble des positions sous la forme d'un
    carré de distance égal à n.
    """
    
    positions = []

    # Add the two lines and two columns without corners
    for i in range(-n + 1, n):
        for coef in {-1, 1}:
            positions.append((i, coef * n))
            positions.append((coef * n, i))

    # Add the 4 corners
    if n <= 1:
        positions.append((0, 0))
    else:    
        positions.append((-n, -n))
        positions.append((-n, n))
        positions.append((n, -n))
        positions.append((n, n))

    return positions

def getMinimalFCost(fCostMatrix):
    """
    Renvoie un couple (x,y) de coordonnées qui correspond au
    cout minimal de la matrice
    """
    x = 0
    y = 0
    while (y < len(fCostMatrix) and fCostMatrix[x][y] != -1):
        x = 0
        while (x < len(fCostMatrix[0]) and fCostMatrix[x][y] != 1):
            x += 1
        y += 1
    
    minCost = fCostMatrix[x][y]
    minCostX = x
    minCostY = y
    while (y < len(fCostMatrix) and fCostMatrix[x][y] != -1):
        x = 0
        while (x < len(fCostMatrix[0]) and fCostMatrix[x][y] != 1):
            if (fCostMatrix[x][y] < minCost):
                minCost = fCostMatrix[x][y]
                minCostX = x
                minCostY = y
            x += 1
        y += 1

    return (minCostX, minCostY)


def getPath(map, startPos, endPos):
    """
    """

    # Contient la liste des cases vertes (pas encore évaluées)
    open = []

    # Contient la liste des cases rouges (non évaluées)
    closed = []

    # Nombre de déplacement pour chaque case
    deplacementCount = [[-1] * map.getDimX()] * map.getDimY()

    gcost = [[-1] * map.getDimX()] * map.getDimY()
    hcost = [[-1] * map.getDimX()] * map.getDimY()
    fcost = [[-1] * map.getDimX()] * map.getDimY()

    parentCase = [[-1] * map.getDimX()] * map.getDimY()
    # La case de départ se caractérise par la valeur None
    parentCase[startPos[0]][startPos[1]] = None

    addPointTo(open, startPos, endPos, startPos, deplacementCount, gcost, hcost, fcost, -1)

    while True:
        current = getMinimalFCost(fcost)
        open.remove(current)
        closed.append(current)

        if (current == endPos):
            break

        for neighbour in getNeighbour(map, current):

            if (neighbour in closed):
                continue

            if neighbour not in open:#ajouter l'autre condition ici
                gcost[neighbour[0]][neighbour[1]] = mathsUtils.distance_tchebychev(startPos, neighbour)
                hcost[neighbour[0]][neighbour[1]] = mathsUtils.distance_tchebychev(neighbour, endPos)
                fcost[neighbour[0]][neighbour[1]] = gcost[neighbour[0]][neighbour[1]] + hcost[neighbour[0]][neighbour[1]]
                parentCase[neighbour[0]][neighbour[1]] = current
                if neighbour not in open:
                    open.append(neighbour)

    parentCasePos = parentCase[endPos[0]][endPos[1]]
    path = []
    while parentCasePos != None:
        path.append(parentCasePos)
        parentCasePos = parentCase[parentCasePos[0]][parentCasePos[1]]

    path.reverse()
    return path

def addPointTo(listToAdd, initPos, endPos, pos, deplacementCount, gcost, hcost, fcost, lastNodeDistance):
    listToAdd.append(pos)
    gcost[pos[0]][pos[1]] = mathsUtils.distance_tchebychev(initPos, pos)
    hcost[pos[0]][pos[1]] = mathsUtils.distance_tchebychev(pos, endPos)
    fcost[pos[0]][pos[1]] = gcost[pos[0]][pos[1]] + hcost[pos[0]][pos[1]]
    deplacementCount[pos[0]][pos[1]] = lastNodeDistance + 1


def getNeighbour(map, pos):
    validNeighbour = []
    for i in {-1, 0, 1}:
        for j in {-1, 0, 1}:
            if (i != 0 and j != 0):
                if map.isAccessible(pos[0] + i, pos[1] + j):
                    validNeighbour.append((pos[0] + i, pos[1] + j))
    return validNeighbour
    