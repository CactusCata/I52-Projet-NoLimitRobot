
import utils.imageUtils as imageUtils
import image.imageManager as imageManager

class Player:

    def __init__(self, robotFile, color):
        """
        color doit etre dans 
        """
        robotFile.load_logo()
        robotIcon = robotFile.get_logo()
        robotIconColored = imageUtils.applyColor(robotIcon, color)
        self.iconTk = imageManager.loadImageTk(robotIconColored)
        self.robotFile = robotFile

    def getIconTk(self):
        return self.iconTk

    def getRobotFile(self):
        return self.robotFile
