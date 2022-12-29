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