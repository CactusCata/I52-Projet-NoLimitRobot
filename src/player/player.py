
import utils.imageUtils as imageUtils
import image.imageManager as imageManager
from robot.robotParty import RobotParty

class Player:

    def __init__(self, robotFile, color, id):

        robotFile.load_bloc()
        robotBloc = robotFile.get_bloc()
        robotBlocColored = imageUtils.applyColor(robotBloc, color)
        self.robotBlocTk = imageManager.loadImageTk(robotBlocColored)

        robotFile.load_icon()
        robotIcon = robotFile.get_icon()
        robotIconColored = imageUtils.applyColor(robotIcon, color)
        self.robotIconTk = imageManager.loadImageTk(robotIconColored)

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
        instruction = ""
        if (self.robotParty.dangerInstructionIsEnabled()):
            instruction = self.robotFile.get_danger_instruction()
            self.robotParty.disable_danger_instruction()
        else:
            instructions = self.robotFile.get_instr()
            instruction = instructions[self.robotParty.get_instruction_number()]
            self.robotParty.update_instruction_cursor((self.robotParty.get_instruction_number() + 1) % len(instructions))
        
        return instruction

    def spawnRobot(self, x, y):
        self.robotParty.move((x, y))


    def getRobotParty(self):
        return self.robotParty

    def getRobotFile(self):
        return self.robotFile

    def getID(self):
        return self.id

    def getRobotBlocTk(self):
        return self.robotBlocTk

    def getRobotIconTk(self):
        return self.robotIconTk

    def getMineBlocTk(self):
        return self.mineBlockTk

    def getRobotFile(self):
        return self.robotFile
