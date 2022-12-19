import utils.otherUtils as otherUtils

from player.player import Player

PLAYER_LIST = []

def initPlayerList():
    """
    Remet à zero la liste des joueurs
    """
    global PLAYER_LIST

    PLAYER_LIST = []

    otherUtils.shuffleColorList()

def addPlayer(robotFile):
    player = Player(robotFile, otherUtils.getColorFromNumber(len(PLAYER_LIST)))
    PLAYER_LIST.append(player)

def updatePlayer(robotFile, index):
    player = Player(robotFile, otherUtils.getColorFromNumber(len(PLAYER_LIST) - 1))
    PLAYER_LIST[index] = player

def getPlayer(n):
    return PLAYER_LIST[n]
