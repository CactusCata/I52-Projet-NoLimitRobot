import frame.rootManager as rootManager

from frame.iFrame import IFrame

from frame.frames.settings.map.fConfigMap import FConfigMap
from frame.frames.settings.robot.fConfigRobot import FConfigRobot
from frame.frames.settings.party.fDeleteParty import FDeleteParty

class FSettings(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()

        buttonConfigMap = super().createButton(text="Configuration des maps", cmd=rootManager.runNewFrame(FConfigMap(self)))
        buttonConfigMap.pack()

        buttonConfigRobot = super().createButton(text="Configuration des robots", cmd=rootManager.runNewFrame(FConfigRobot(self)))
        buttonConfigRobot.pack()

        buttonDeleteParty = super().createButton(text="Supprimer une partie", cmd=rootManager.runNewFrame(FDeleteParty(self)))
        buttonDeleteParty.pack()

        comboBoxFullScreen = super().createCheckButton(text="Plein ecran", callback=self.toggleFullScreen)
        comboBoxFullScreen.pack()

        comboBoxEnableHelp = super().createCheckButton(text="Activer l'aide", callback=self.toggleHelp)
        comboBoxEnableHelp.pack()

        buttonBack = super().createButton(text="Retour", cmd=super().reopenLastFrame)
        buttonBack.pack()

    def toggleFullScreen(self):
        print("Fullscreen is toggled")

    def toggleHelp(self):
        print("Help has been toggled")