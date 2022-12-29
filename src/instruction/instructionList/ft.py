from instruction.instructionList.iInstruction import IInstruction

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

        pathsToNextCase = []
        for i in {-1, 0, 1}:
            for j in {-1, 0, 1}:
                if (i != 0 and j != 0):
                    if map.isAccessible(robot.get_x() + i, robot.get_y() + j):
                        pathsToNextCase.append(map.getPath((robot.get_x() + i, robot.get_y() + j), (nearestRobot.get_x(), nearestRobot.get_y())))

        farestPath = pathsToNextCase[0]
        for i in range(len(pathsToNextCase)):
            if len(farestPath) > len(pathsToNextCase[i]):
                farestPath = pathsToNextCase[i]

        nextCase = farestPath[0]

        map.updateRobotPosition(robot, nextCase)
