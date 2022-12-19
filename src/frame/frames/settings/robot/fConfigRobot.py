import frame.rootManager as rootManager

from frame.iFrame import IFrame, help_activated
from frame.messagesHelp import HELP_FCONFIGROBOT

from frame.frames.settings.robot.fCreateRobot import FCreateRobot
from frame.frames.settings.robot.fEditRobot import FEditRobot
from frame.frames.settings.robot.fDeleteRobot import FDeleteRobot

class FConfigRobot(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()


        buttonCreateRobot = super().createButton(text="Créer robot", cmd=lambda:rootManager.runNewFrame(FCreateRobot(self)))
        buttonCreateRobot.pack()

        buttonEditRobot = super().createButton(text="Editer robot", cmd=lambda:rootManager.runNewFrame(FEditRobot(self)))
        buttonEditRobot.pack()

        buttonDeleteRobot = super().createButton(text="Supprimer robot", cmd=lambda:rootManager.runNewFrame(FDeleteRobot(self)))
        buttonDeleteRobot.pack()

        if help_activated == True:
            buttonHelp = super().createButtonHelp(master = root, msg=HELP_FCONFIGROBOT)
            buttonHelp.pack()

        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FConfigRobot, self).reopenLastFrame())
        buttonBack.pack()
