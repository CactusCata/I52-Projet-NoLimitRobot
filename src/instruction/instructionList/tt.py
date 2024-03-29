from instruction.instructionList.iInstruction import IInstruction

import utils.instructionUtils as instructionUtils

class TT(IInstruction):
    """
    Fonction de test de repérage. Si le robot ennemi le plus proche est à une
    distance inférieur ou égale à la distance de repérage des robots, alors
    on exécute la première instruction, sinon la deuxième si supérieur.
    """

    def __init__(self):
        super().__init__("ft", 4, resume="test de proximité", message="Appel de l'instruction de test, elle conditionne l'appel à des instructions déjà citées (AL, MI, IN, PS et FT) et à deux nouvelles instructions (TH, TV, voir ci-dessous). Ce test est un test de distance : il détermine si le robot adverse le plus proche est ou non situé à une distance inférieure ou égale à celle définie comme “distance de repérage”. Si la réponse est oui le robot effectuera l'action correspondant à l'instruction qui suit immédiatement l'instruction TT, sinon il suivra la deuxième instruction qui suit l'instruction TT (exemple : TT MI PS, ce qui se traduit par si le robot le plus proche est à une distance inférieure ou égale à celle de repérage alors pose d'une mine sinon poursuite de ce robot).")

    def make(self, **kargs):
        """
        Paramètre: robot, map, instructionName1, instructionName2
        """
        player = kargs["player"]
        robot = player.getRobotParty()
        map = kargs["map"]
        command = kargs["cmd"]
        instructionName1 = command.split(" ")[1]
        instructionName2 = command.split(" ")[2]

        super().decreaseRobotEnergy(robot)

        nearestRobotPath = map.getNearestRobot(robot)[1]

        if nearestRobotPath == None or len(nearestRobotPath) == 0:
            return
        
        # Si le un robot est proche, executer l'instruction 1
        # Sinon excuter l'instruction 2
        if (len(nearestRobotPath) <= robot.get_distance_detect()):
            instructionUtils.INSTRUCTION_LIST[instructionName1].make(player=player, robot=robot, map=map, cmd=instructionName1)
        else:
            instructionUtils.INSTRUCTION_LIST[instructionName2].make(player=player, robot=robot, map=map, cmd=instructionName1)