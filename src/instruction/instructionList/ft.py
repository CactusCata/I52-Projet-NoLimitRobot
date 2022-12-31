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

        print(f"Current robot pos: {robot.get_x()}, {robot.get_y()}")
        nearestRobot = map.getNearestRobot(robot)[0]
        print(f"nearest robot pos: {nearestRobot.get_x()}, {nearestRobot.get_y()}")


        neighboors = mapUtils.getNeighbour(map, (robot.get_x(), robot.get_y()))

        farestPathLength = -1
        bestCase = (-1, -1)
        for neighboor in neighboors:
            path = mapUtils.getPath(map, neighboor, (nearestRobot.get_x(), nearestRobot.get_y()))
            pathLength = len(path)
            if pathLength > farestPathLength:
                farestPathLength = pathLength
                bestCase = neighboor


        map.updateRobotPosition(robot, bestCase)
