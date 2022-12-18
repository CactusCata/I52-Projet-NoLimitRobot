from instruction.instructionList.iInstruction import IInstruction

import random

class MI(IInstruction):
    """
    Le robot pose une mine autour de lui de manière aléatoire. Si obstacle il y a,
    il est dans l'incapacité de poser à nouveau une mine.
    """

    def __init__(self):
        super().__init__("mi", 10, damage=200, resume="pose d’une mine", message="Pose d'une mine sur l'une des quatre cases voisines du robot (au hasard). C'est l'arme la plus meurtrière pour les robots adverses. Quand ils marchent sur une de vos mines, ils perdent 200 points d'énergie. En outre, le pas de leur programme au moment de l'explosion est détruit et remplacé par celui du “circuit de secours” (voir ce paragraphe). Les robots sont capables de reconnaître leurs propres mines et ne sautent pas sur elles mais celles-ci sont détruites dans tous les cas de figure.")

    def make(self, **kargs):
        """
        Paramètre: robot, map
        """
        robot = kargs["robot"]
        map = kargs["map"]

        super().decreaseRobotEnergy(robot)

        minesPosition = []

        for i in {-1, 1}:
            if map.isAccessible(robot, (robot.getX() + i, robot.getY())): minesPosition.append((robot.getX() + i, robot.getY()))
            if map.isAccessible(robot, (robot.getX(), robot.getY() + i)): minesPosition.append((robot.getX(), robot.getY() + i))

        choosedMinePosition = minesPosition[random.randint(0, len(minesPosition) - 1)]

        map.placeMine(choosedMinePosition)
