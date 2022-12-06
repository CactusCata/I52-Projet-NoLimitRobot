from tkinter.filedialog import askopenfile

import frame.rootManager as rootManager
from frame.frames.settings.robot.fEditRobot import FEditRobot

from frame.iFrame import IFrame

class FCreateRobot(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()

        NameChoice = super().createFrame(root)
        NameChoice.pack()
        textName = super().createLabel(NameChoice, "Nom de ton robot mon cheum (O_O) :\t")
        textName.pack(side="left")
        textboxName = super().createTextBox(NameChoice)
        textboxName.pack(side="right")

        DescOptionnal = super().createFrame(root) #choix optionnel
        DescOptionnal.pack()
        textDescription = super().createLabel(DescOptionnal, "(Optionnel)\t")
        textDescription.pack(side="left")
        textboxDescription = super().createTextBox(DescOptionnal)
        textboxDescription.pack(side="right")

        PathOptionnal = super().createFrame(root) #choix optionnel
        PathOptionnal.pack()
        textPath = super().createLabel(PathOptionnal, "(Optionnel)\t")
        textPath.pack(side="left")
        buttonPath = super().createButton(PathOptionnal,text="Sélectionner votre Robot", cmd=lambda:self.selecPath()) #filedialog.askopenfile(mode='r')
        buttonPath.pack(side="right")

        buttonConfirm = super().createButton(text="Confirmer", cmd=lambda:rootManager.runNewFrame(FEditRobot(self)))
        buttonConfirm.pack()

        buttonHelp = super().createButton(text="Aide")
        buttonHelp.pack()

        buttonBack = super().createButton(text="Retour", cmd=lambda:(FConfigRobot, self).reopenLastFrame)
        buttonBack.pack()



    def selecPath(self):

        selectedfile = askopenfile(mode='r')
