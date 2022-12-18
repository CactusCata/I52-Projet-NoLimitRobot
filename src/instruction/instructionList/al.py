from instruction.instructionList.iInstruction import IInstruction

import random

class AL(IInstruction):
    """
    Déplace le robot dans une direction aléatoire si il n'y a pas de rocher
    ou de robot.
    Celui-ci dépense donc 5 d'énergie, et s'il marche/roule sur une mine,
    il perd 200 d'énergie et rentre dans le mode de secours de par la
    fonction danger()
    """

    def __init__(self):
        super().__init__("AL", 1, resume="déplacement aléatoire", message="Déplacement aléatoire d'une case dans une direction aléatoire si la case visée est libre sinon reste sur place (permet de rompre des séquences de programmation conduisant au blocage).")


    def make(self, **kargs):
        """
        Paramètre: robot, map
        """
        robot = kargs["robot"]
        map = kargs["map"]

        super().decreaseRobotEnergy(robot)

        possiblesMoves = []

        for i in {-1, 1}:
            if map.isAccessible(robot, (robot.getX() + i, robot.getY())): possiblesMoves.append((robot.getX() + i, robot.getY()))
            if map.isAccessible(robot, (robot.getX(), robot.getY() + i)): possiblesMoves.append((robot.getX(), robot.getY() + i))

        choosedMove = possiblesMoves[random.randint(0, len(possiblesMoves) - 1)]

        map.updateRobotPosition(robot, choosedMove)
        robot.move(choosedMove)