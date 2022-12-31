import math
import random

import utils.mathsUtils as mathsUtils

def getRandomValideRobotPosition(map):
    """
    Renvoie une position aléatoire valide sur la map
    """
    position = (random.randint(0, map.getDimX() - 1), random.randint(0, map.getDimY() - 1))
    while (not map.isAccessible(position)):
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

    robotsPositions = []
    mapDimX = map.getDimX()
    mapDimY = map.getDimY()

    for i in range(playerAmount):
        alpha = (2 * math.pi * i) / playerAmount
        robotPosition = (int((1 + math.cos(alpha)) * mapDimX * 0.4), int((1 + math.sin(alpha)) * mapDimY * 0.4))
        robotPosition = generateValideRobotPosition(map, robotPosition)
        robotsPositions.append(robotPosition)

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
    minCost = 10000
    minCostX = 0
    minCostY = 0
    for x in range(len(fCostMatrix)):
        for y in range(len(fCostMatrix[0])):
            current = fCostMatrix[x][y]
            if (current != -1 and current < minCost):
                minCost = current
                minCostX = x
                minCostY = y

    return (minCostX, minCostY)

def generateRobotEndPos(map, endPos):
    endPosNeighbour = getNeighbour(map, endPos)
    if len(endPosNeighbour) == 0:
        return None

    return random.choice(endPosNeighbour)

def getPath(map, startPos, endPos):
    """
    """

    if (not map.isAccessible(endPos)):
        endPos = generateRobotEndPos(map, endPos)

    if endPos == None:
        return []

    # Contient la liste des cases vertes (pas encore évaluées)
    open = []

    # Contient la liste des cases rouges (non évaluées)
    closed = []

    # Nombre de déplacement pour chaque case
    deplacementCount = []
    gcost = []
    hcost = []
    fcost = []
    parentCase = []
    for i in range(map.getDimX()):
        deplacementCount.append([-1] * map.getDimY())
        gcost.append([-1] * map.getDimY())
        hcost.append([-1] * map.getDimY())
        fcost.append([-1] * map.getDimY())
        parentCase.append([-1] * map.getDimY())

    # La case de départ se caractérise par la valeur None
    parentCase[startPos[0]][startPos[1]] = None

    addPointTo(open, startPos, endPos, startPos, deplacementCount, gcost, hcost, fcost, None)

    while True:
        current = getMinimalFCost(fcost)
        if (current not in open):
            return []
        open.remove(current)
        gcost[current[0]][current[1]] = -1
        hcost[current[0]][current[1]] = -1
        fcost[current[0]][current[1]] = -1
        closed.append(current)

        if (current == endPos):
            break

        for neighbour in getNeighbour(map, current):

            if (neighbour in closed):
                continue

            if neighbour not in open:#ajouter l'autre condition ici
                addPointTo(open, startPos, endPos, neighbour, deplacementCount, gcost, hcost, fcost, deplacementCount[current[0]][current[1]])
                parentCase[neighbour[0]][neighbour[1]] = current

    parentCasePos = parentCase[endPos[0]][endPos[1]]
    path = [endPos]
    while parentCasePos != None:
        path.append(parentCasePos)
        parentCasePos = parentCase[parentCasePos[0]][parentCasePos[1]]

    path.reverse()
    return path

def addPointTo(listToAdd, initPos, endPos, pos, deplacementCount, gcost, hcost, fcost, lastNodeDistance):
    if pos not in listToAdd:
        listToAdd.append(pos)
    gcost[pos[0]][pos[1]] = mathsUtils.distance_chareyre(initPos, pos)
    hcost[pos[0]][pos[1]] = mathsUtils.distance_chareyre(pos, endPos)
    fcost[pos[0]][pos[1]] = gcost[pos[0]][pos[1]] + hcost[pos[0]][pos[1]]
    if lastNodeDistance == None:
        lastNodeDistance = -1
    deplacementCount[pos[0]][pos[1]] = lastNodeDistance + 1


def getNeighbour(map, pos):
    validNeighbour = []
    for i in {-1, 0, 1}:
        for j in {-1, 0, 1}:
            if (i != 0 or j != 0):
                if map.isAccessible((pos[0] + i, pos[1] + j)):
                    validNeighbour.append((pos[0] + i, pos[1] + j))
    return validNeighbour
    