import utils.imageUtils as imageUtils
import image.imageManager as imageManager
from robot.robotParty import RobotParty

class Player:
    """
    Classe du joueur
    """

    def __init__(self, robotFile, color, id):
        """
            - robotFile: instance de RobotFile
            - color: triplet RGB
            - id: numero du joueur
        """

        # Chargement du bloc du robot
        robotFile.load_bloc()
        robotBloc = robotFile.get_bloc()
        robotBlocColored = imageUtils.applyColor(robotBloc, color)
        self.robotBlocTk = imageManager.loadImageTk(robotBlocColored)

        # Chargement du logo du robot
        robotFile.load_icon()
        robotIcon = robotFile.get_icon()
        robotIconColored = imageUtils.applyColor(robotIcon, color)
        self.robotIconTk = imageManager.loadImageTk(robotIconColored)

        # Chargement du logo coloré de la mine
        mineBloc = imageManager.IMG_MAP_MINE
        mineBlocColored = imageUtils.applyColor(mineBloc, color)
        self.mineBlockTk = imageManager.loadImageTk(mineBlocColored)

        self.robotFile = robotFile
        self.id = id
        self.robotParty = RobotParty(-1, -1)

    def getNextInstructionName(self):
        """
        Renvoie la prochaine instruction du robot associé au joueur
        et passe à l'instruction d'après
        """

        instructions = self.robotFile.get_instr()
        instruction = instructions[self.robotParty.get_instruction_number()]
        self.robotParty.update_instruction_cursor((self.robotParty.get_instruction_number() + 1) % len(instructions))
        
        return instruction

    def spawnRobot(self, x, y):
        """
        Fait apparaitre le robot à certaines coordonées
        """
        self.robotParty.move((x, y))

    def enable_danger_instruction(self):
        """
        Activé lorsque le robot du joueur marche sur une mine
        """
        self.robotFile.enable_danger_instruction(self.robotParty.get_instruction_number())

    def getRobotParty(self):
        """
        Renvoie l'instance du RobotParty
        """
        return self.robotParty

    def getRobotFile(self):
        """
        Renvoie l'instance du RobotFile
        """
        return self.robotFile

    def getID(self):
        """
        Renvoie le numero du joueur
        """
        return self.id

    def getRobotBlocTk(self):
        """
        Renvoie le bloc du robot
        """
        return self.robotBlocTk

    def getRobotIconTk(self):
        """
        Renvoie l'icon du robot
        """
        return self.robotIconTk

    def getMineBlocTk(self):
        """
        Renvoie le bloc de la mine coloré du robot
        """
        return self.mineBlockTk
