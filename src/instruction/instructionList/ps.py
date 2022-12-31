from instruction.instructionList.iInstruction import IInstruction

class PS(IInstruction):
    """
    Déplace le robot courant d'une case dans la direction du robot le plus
    proche. Si tested vaut True, alors un test de distance de repérage sera
    fait.
    """

    def __init__(self):
        super().__init__("ps", 4, resume="poursuite", message="Instruction de poursuite, votre robot doit repérer l'adversaire le plus proche, puis se diriger d'une case vers lui. Le déplacement, s'il est possible, peut s'effectuer en diagonale, contrairement aux autres types de déplacement. Si elle n'est pas conditionnée par l'instruction de test (TT), cette instruction s'effectue quelle que soit la distance qui sépare votre robot de l'adversaire le plus proche.")

    def make(self, **kargs):
        """
        Paramètre: robot, map
        """
        player = kargs["player"]
        robot = player.getRobotParty()
        map = kargs["map"]

        super().decreaseRobotEnergy(robot)

        nearestRobotPath = map.getNearestRobot(robot)[1]
        print(f"PS: nearestRobotPath: {nearestRobotPath}")
        if len(nearestRobotPath) > 1:
            nextCase = nearestRobotPath[1]
            map.updateRobotPosition(robot, nextCase)
