from instruction.instructionList.iInstruction import IInstruction

import random

class TV(IInstruction):
    """
    Tire 
    """

    def __init__(self):
        super().__init__("tv", 3, damage=20, resume="tir vertical", message="Tir vertical, en haut ou en bas aléatoirement, Le tir est stoppé par la première cible (obstacle, robot ou mine) rencontrée. Il permet d'affaiblir vos adversaires car un robot touché perd 20 points d'énergie. Ils détruisent les mines adverses rencontrées, sans détruire les vôtres. Il est sans effet sur les obstacles.")


    def make(self, **kargs):
        """
        Paramètre: robot, map
        """
        robot = kargs["robot"]
        map = kargs["map"]

        super().decreaseRobotEnergy(robot)

        possiblesDirection = ['H', 'B']
        selectedDirection = possiblesDirection[random.randint(0, len(possiblesDirection) - 1)]
        map.robotShoot(robot, selectedDirection)