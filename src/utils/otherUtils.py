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

def convertHealthPercentToColor(healthPercent):
    """
    healthPercent: nombre E [0;100]
    Renvoie le code hexadécimal de la couleur correspondant
    au pourcentage de point de vie
    """
    r = min(255, 255 - int((healthPercent - 50) * (255 / 50)))
    g = min(255, int(healthPercent * (255 / 50)))
    b = 0
    return '#%02x%02x%02x' % (r, g, b)

if __name__ == "__main__":
    for healthPercent in (100, 75, 51, 50, 49, 25, 1, 0):
        print(f"HealthPercent: {healthPercent}")
        print(f"res: {convertHealthPercentToColor(healthPercent)}")