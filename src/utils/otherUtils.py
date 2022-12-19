import random

COLORS = [
    (255, 127, 0), # orange
    (255, 127, 255), # rose
    (0, 127, 255), # bleu
    (0, 255, 0), # vert
    (255, 0, 0), # rouge
    (0, 255, 255) # aqua
]

def shuffleColorList():
    random.shuffle(COLORS)

def getColorFromNumber(n):
    """
    Renvoie la n-ième couleur de la liste 
    """
    return COLORS[n]