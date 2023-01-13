from instruction.instructionList.iInstruction import IInstruction

import utils.mapUtils as mapUtils

class FT(IInstruction):
    """
    Déplace le robot courant d'une case dans la direction opposée au robot le
    plus proche.Si tested vaut True, alors un test de distance de repérage sera
    fait.
    """

    # NOTE: PEUT ETRE FAIRE UNE MATRICE DE PRESENCE, PLUS OPTI ET MIEUX
    # chaque case contient la somme des distances des robots

    def __init__(self):
        super().__init__("ft", 4, resume="fuite", message="Instruction de fuite, comme l'instruction PS, mais le robot fuit l'adversaire le plus proche au lieu de le poursuivre.")

    def make(self, **kargs):
        """
        Paramètre: robot, map
        """
        player = kargs["player"]
        robot = player.getRobotParty()
        map = kargs["map"]

        super().decreaseRobotEnergy(robot)

        nearestRobot = map.getNearestRobot(robot)

        if (nearestRobot == None or len(nearestRobot) == 0):
            return

        nearestRobot = nearestRobot[0]
        
        # Append if all others robots are vanished
        if (nearestRobot == None):
            return

        # Listes des cases disponibles autour du robot 
        neighboors = mapUtils.getNeighbour(map, (robot.get_x(), robot.get_y()))

        # Choisi la case qui ajoutera le plus
        # de chemin à faire pour le robot aux alentours
        farestPathLength = -1
        bestCase = (-1, -1)
        for neighboor in neighboors:
            path = mapUtils.getPath(map, neighboor, (nearestRobot.get_x(), nearestRobot.get_y()))
            pathLength = len(path)
            if pathLength > farestPathLength:
                farestPathLength = pathLength
                bestCase = neighboor


        map.updateRobotPosition(robot, bestCase)
