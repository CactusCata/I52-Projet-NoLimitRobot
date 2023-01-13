import math

def distance_euclydienne(xa, ya, xb, yb):
    """
    Renvoie la distance euclydienne entre le point (xa, ya) et (xb, yb).
    """
    return math.sqrt(math.pow(xb - xa, 2) + math.pow(yb - ya, 2))

def distance_tchebychev(posA, posB):
    """
    Renvoie la distance de Tchebychev
    """
    return max(abs(posB[0] - posA[0]), abs(posB[1] - posA[1]))

def distance_chareyre(posA, posB):
    """
    Renvoie la distance de Chareyre
    """
    return distance_tchebychev(posA, posB) + 0.1 * distance_euclydienne(posA[0], posA[1], posB[0], posB[1])