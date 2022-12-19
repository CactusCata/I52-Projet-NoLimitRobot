import math

def distance(xa, ya, xb, yb):
    """
    Renvoie la distance euclydienne entre le point (xa, ya) et (xb, yb).
    """
    return math.sqrt(math.pow(xb - xa, 2) + math.pow(yb - ya, 2))