from instruction.instructionList.iInstruction import IInstruction

import random

class IN(IInstruction):
    """
    Met le robot dans l'état invisible pour le tour de cette instruction.
    """

    def __init__(self):
        super().__init__("in", 20, resume="invisibilité", message="Invisibilité, c'est une contre-mesure électronique qui coûte cher en énergie, mais qui déboussole complètement les adversaires. Au moment où votre robot utilise cette instruction, les autres robots ne savent plus où il est.")

    def make(self, **kargs):
        """
        Paramètre: robot, map
        """
        robot = kargs["robot"]

        super().decreaseRobotEnergy(robot)
        robot.vanish()