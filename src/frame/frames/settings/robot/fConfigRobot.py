import frame.rootManager as rootManager

from frame.iFrame import IFrame

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

        buttonHelp = super().createButton(text="Aide")
        buttonHelp.pack()

        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FConfigRobot, self).reopenLastFrame())
        buttonBack.pack()