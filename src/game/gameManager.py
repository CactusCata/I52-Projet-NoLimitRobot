import player.playerManager as playerManager
import map.map as map
import utils.instructionUtils as instructionUtils

ENERGY_PER_ROBOT = -1
ROBOT_DETECTION_DISTANCE = -1
MAP_CHOOSED = None
PLACEMENT_METHOD = None
SPREAD_ROBOT_DISTANCE = -1

def setEnergyPerRobot(energy):
    global ENERGY_PER_ROBOT

    ENERGY_PER_ROBOT = energy

def setRobotDistanceDetection(distance):
    global ROBOT_DETECTION_DISTANCE

    ROBOT_DETECTION_DISTANCE = distance

def setPartyMap(map):
    """
    map: de type map
    """
    global MAP_CHOOSED

    MAP_CHOOSED = map

def setPlacementMethod(placementMethod):
    global PLACEMENT_METHOD

    PLACEMENT_METHOD = placementMethod

def setSpreadRobotDistance(distance):
    global SPREAD_ROBOT_DISTANCE

    SPREAD_ROBOT_DISTANCE = distance


def calculateGame():
    playersAlive = playerManager.PLAYER_LIST
    currentMap = MAP_CHOOSED

    mapIDHistory = []
    mapInstanceHistory = []

    mapIDHistory.append(currentMap.copyMapID())
    mapInstanceHistory.append(currentMap.copyMapInstance())

    # Calculer la partie tant qu'au moins encore 2 robots
    # sont en vie
    while len(playersAlive) > 1:
        i = 0

        # On itère à travers les joueurs encore en vie
        while i < len(playersAlive) and len(playersAlive) > 1:
            player = playersAlive[i]
            robot = player.getRobot()

            if (robot.get_energy() <= 0):
                playersAlive.remove(player)
                continue

            instructionName = robot.getNextInstructionName()
            instruction = instructionUtils.INSTRUCTION_LIST[instructionName]
            instruction.make(player=player, map=currentMap, cmd=instructionName)
