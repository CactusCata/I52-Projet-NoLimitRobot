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


        pathsToNextCase = []
        neighboors = mapUtils.getNeighbour(map, (robot.get_x(), robot.get_y()))
        for neighboor in neighboors:
            print(f"({neighboor[0]}, {neighboor[1]}) --> ({nearestRobot.get_x()}, {nearestRobot.get_y()}) = ")
            path = mapUtils.getPath(map, neighboor, (nearestRobot.get_x(), nearestRobot.get_y()))
            print(path)
            pathsToNextCase.append((neighboor, path))

        print(pathsToNextCase)
        farestPathData = pathsToNextCase[0]
        for i in range(len(pathsToNextCase)):
            if len(farestPathData[1]) < len(pathsToNextCase[i][1]) and len(pathsToNextCase[i][1]) != 0:
                farestPathData = pathsToNextCase[i]

        print(f"Selected path is : {farestPathData[1]}")

        nextCase = (farestPathData[0][0], farestPathData[0][1])

        map.updateRobotPosition(robot, nextCase)
