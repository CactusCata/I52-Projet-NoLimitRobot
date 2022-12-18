from instruction.instructionList.iInstruction import IInstruction

class DD(IInstruction):
    """
    Déplace le robot dans la direction donnée si il n'y a pas de rocher ou de
    robot. Retourne True si déplacement fait, False sinon.
    Celui-ci dépense donc 5 d'énergie, et s'il marche/roule sur une mine,
    il perd 200 d'énergie et rentre dans le mode de secours de par la
    fonction danger()
    """

    def __init__(self):
        super().__init__("DD", 5, resume="déplacement choisi", message="Déplacement déterministe d'une case dans une direction fournie (H : haut, B : bas, D : droite, G : gauche) si la case visée est libre sinon reste sur place. C'est une instruction importante pour les terrains dégagés.")


    def make(self, **kargs):
        """
        Paramètre: robot, map, direction
        """
        robot = kargs["robot"]
        direction = kargs["direction"]
        map = kargs["map"]

        super().decreaseRobotEnergy(robot)

        targetCase = (-1, -1)
        if (direction == 'H'): targetCase = (robot.getX(), robot.getY() - 1)
        elif (direction == 'B'): targetCase = (robot.getX(), robot.getY() + 1)
        elif (direction == 'G'): targetCase = (robot.getX() - 1, robot.getY())
        elif (direction == 'D'): targetCase = (robot.getX() + 1, robot.getY())

        if (not map.isAccessible(targetCase)):
            return False

        map.updateRobotPosition(robot, targetCase)
        robot.move(targetCase)



