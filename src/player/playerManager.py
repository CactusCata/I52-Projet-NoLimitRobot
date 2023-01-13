import utils.otherUtils as otherUtils

from player.player import Player

# Dimensions de l'image de l'icon d'un robot
PLAYER_ICON_DIMENSIONS = (40, 40)

# Liste des joueurs
PLAYER_LIST = []

def initPlayerList():
    """
    Remet à zero la liste des joueurs
    """
    global PLAYER_LIST

    PLAYER_LIST = []

    otherUtils.shuffleColorList()

def addPlayer(robotFile):
    """
    Permet d'ajouter un robot
    """
    player = Player(robotFile, otherUtils.getColorFromNumber(len(PLAYER_LIST)), len(PLAYER_LIST))
    PLAYER_LIST.append(player)

def updatePlayer(robotFile, index):
    """
    Met à jour le robot d'un joueur
    """
    player = Player(robotFile, otherUtils.getColorFromNumber(len(PLAYER_LIST) - 1), len(PLAYER_LIST) - 1)
    PLAYER_LIST[index] = player

def getPlayer(n):
    return PLAYER_LIST[n]
