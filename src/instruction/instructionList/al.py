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
        player = kargs["player"]
        robot = player.getRobotParty()
        map = kargs["map"]

        super().decreaseRobotEnergy(robot)

        # Liste des déplacements possibles
        possiblesMoves = []
        for i in {-1, 1}:
            if map.isAccessible((robot.get_x() + i, robot.get_y())): possiblesMoves.append((robot.get_x() + i, robot.get_y()))
            if map.isAccessible((robot.get_x(), robot.get_y() + i)): possiblesMoves.append((robot.get_x(), robot.get_y() + i))

        # Si aucun déplacement possible (coincé), alors
        # annuler le déplacement
        if (len(possiblesMoves) == 0):
            return

        choosedMove = random.choice(possiblesMoves)

        map.updateRobotPosition(robot, choosedMove)