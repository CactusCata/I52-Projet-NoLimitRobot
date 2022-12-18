from tkinter.filedialog import askopenfile

import frame.rootManager as rootManager
from frame.frames.settings.robot.fEditRobot import FEditRobot
import robot.robotManager as robotManager

from frame.iFrame import IFrame

from tkinter import END

class FCreateRobot(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()

        # Nom du robot
        textName = super().createLabel(text="Nom du robot:")
        textName.pack()
        self.entryName = super().createEntry(width=15)
        self.entryName.pack()

        # Description
        textDescription = super().createLabel(text="Description (Optionnelle):")
        textDescription.pack()
        self.entryDescription = super().createEntry(width=50)
        self.entryDescription.pack()

        # Logo
        logoLabel = super().createLabel(text="Logo (Optionnel):")
        logoLabel.pack()
        logoButtonChooseLogoPath = super().createButton(text="Sélectionnez votre Logo", cmd=lambda:self.selectLogoPath())
        logoButtonChooseLogoPath.pack()
        self.entryLogoPath = super().createEntry(width=40)
        self.entryLogoPath.pack()

        # Confirmer
        buttonConfirm = super().createButton(text="Editer le robot", cmd=lambda:self.followingFrame())
        buttonConfirm.pack()

        # Aide
        buttonHelp = super().createButton(text="Aide")
        buttonHelp.pack()

        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FCreateRobot, self).reopenLastFrame())
        buttonBack.pack()

    def selectLogoPath(self):
        """
        Demande à l'utilisateur une image pour la copier coller dans le répertoire des
        images de robots, afin d'avoir une trace permanente des images des robots.
        L'image en .png possède le même nom que le répertoire de ce dit robot.
        """
        file = askopenfile(mode='r')
        if (file != None):
            self.entryLogoPath.delete(0, "end")
            self.entryLogoPath.insert(0, file.name)

    def followingFrame(self):
        """
        S'occupe de passer à la prochaine fenêtre ou non, en fonction des
        différentes erreurs présentes
        """
        robotName = self.entryName.get()
        description = self.entryDescription.get()
        logoPath = self.entryLogoPath.get()

        print(f"filename: \"{robotName}\"")
        print(f"description: \"{description}\"")
        print(f"logopath: \"{logoPath}")

        if len(robotName) == 0:
            self.createMessage("Vous n'avez pas donné de nom à votre robot !")
            return

        if robotName in robotManager.getLoadedRobots():
            self.createMessage("Le nom du robot est déjà utilisé")
            return

        robotManager.createNewRobot(robotName, description, [], logoPath)
        rootManager.runNewFrame(FEditRobot(self))

    def error(self, widget): #Erreur si l'utilisateur n'a pas mit de nom
        widget.destroy()

    def createMessage(self, message):
        labelerror = super().createLabel(message, 30)
        labelerror["fg"] = "#FA0000"
        labelerror.pack()
        labelerror.after(5000, lambda:self.error(labelerror))