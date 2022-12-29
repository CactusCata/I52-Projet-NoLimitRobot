from instruction.instructionList.iInstruction import IInstruction

import random

class TH(IInstruction):
    """
    Déplace le robot dans une direction aléatoire si il n'y a pas de rocher
    ou de robot.
    Celui-ci dépense donc 5 d'énergie, et s'il marche/roule sur une mine,
    il perd 200 d'énergie et rentre dans le mode de secours de par la
    fonction danger()
    """

    def __init__(self):
        super().__init__("TH", 3, damage=20, resume="tir vertical", message="Tir horizontal, à gauche ou à droite aléatoirement. Le tir est stoppé par la première cible (obstacle, robot ou mine) rencontrée. Il permet d’affaiblir vos adversaires car un robot touché perd 20 points d’énergie. Ils détruisent les mines adverses rencontrées, sans détruire les vôtres. Il est sans effet sur les obstacles.")


    def make(self, **kargs):
        """
        Paramètre: robot, map
        """
        player = kargs["player"]
        robot = player.getRobotParty()
        map = kargs["map"]

        super().decreaseRobotEnergy(robot)

        possiblesDirection = ['G', 'D']
        selectedDirection = random.choice(possiblesDirection)
        map.robotShoot(robot, selectedDirection)