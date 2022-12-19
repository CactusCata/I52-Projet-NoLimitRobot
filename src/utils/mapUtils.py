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
    
    robotsPositions = []
    mapDimX = map.getDimX()
    mapDimY = map.getDimY()

    for i in range(playerAmount):
        alpha = (2 * math.pi * i) / playerAmount
        robotPosition = (int(math.cos(alpha) * mapDimX * 0.8)), int((math.sin(alpha) * mapDimY * 0.8))
        robotPosition = generateValideRobotPosition(map, robotPosition)
        robotsPositions.append(robotPosition)

    return robotPosition

def generateValideRobotPosition(map, robotPosition):
    """
    Génère une position valide autour d'un point pour le robot
    dont la position est robotPosition.
    """
    validposition = None
    j = 0
    while not hasFoundPossiblePosition:
        possiblesPositions = generateSquarePositions(j)
        random.shuffle(possiblesPositions)

        k = 0
        while k < len(possiblesPositions) and not hasFoundPossiblePosition:
            currentSelectedPosition = possiblesPositions[k]

            # Si la case est accessible, on arrête la recherche de case valide
            if map.isAccessible(robotPosition[0] + currentSelectedPosition[0], robotPosition[1] + currentSelectedPosition):
                validposition = (robotPosition[0] + currentSelectedPosition[0], robotPosition[1] + currentSelectedPosition)
                hasFoundPossiblePosition = True
            
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