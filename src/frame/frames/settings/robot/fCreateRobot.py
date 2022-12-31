from tkinter.filedialog import askopenfile

import frame.rootManager as rootManager
from frame.frames.settings.robot.fEditRobot import FEditRobot
import robot.robotManager as robotManager

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FCREATEROBOT

import tkinter as tk
from tkinter import END
import utils.tkinter.tkUtils as tkUtils

class FCreateRobot(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FCREATEROBOT)

    def draw(self):
        root = rootManager.getRoot()

        # Aide
        super().createButtonHelp()
        #

        frameMain = super().createFrame(root)
        frameMain.pack()

        # Nom du robot
        frameNameRobot = super().createFrame(frameMain)
        frameNameRobot.pack(pady = tkUtils.ratioHeight(0.04, root), fill=tk.X)
        textName = super().createLabel(master=frameNameRobot, text="Nom du robot:")
        textName.pack(side="left")
        self.entryName = super().createEntry(master=frameNameRobot, width=15)
        self.entryName.pack(fill=tk.X)
        #

        # Description
        frameDescription = super().createFrame(frameMain)
        frameDescription.pack(pady = tkUtils.ratioHeight(0.04, root), fill=tk.X)
        textDescription = super().createLabel(master=frameDescription, text="Description (Optionnelle):")
        textDescription.pack(side="left")
        self.entryDescription = super().createEntry(master=frameDescription, width=tkUtils.ratioWidth(0.04, root))
        self.entryDescription.pack(fill=tk.X)
        #

        # Logo
        frameLogoSelected = super().createFrame(frameMain)
        frameLogoSelected.pack(pady = tkUtils.ratioHeight(0.04, root), fill=tk.X)
        logoLabelOptionnal = super().createLabel(master=frameLogoSelected, text="Logo (Optionnel):")
        logoLabelOptionnal.pack(side="left")
        logoButtonChooseLogoPath = super().createButton(master=frameLogoSelected, text="Sélectionnez votre Logo", cmd=lambda:self.selectLogoPath())
        logoButtonChooseLogoPath.pack(fill=tk.X)

        frameLogoPath = super().createFrame(frameMain)
        frameLogoPath.pack(fill=tk.X)
        logoLabelPath = super().createLabel(master=frameLogoPath, text="Chemin absolu de votre logo:")
        logoLabelPath.pack(side="left")
        self.entryLogoPath = super().createEntry(master=frameLogoPath, width=tkUtils.ratioWidth(0.04, root))
        self.entryLogoPath.pack(fill=tk.X)
        #

        # Confirmer
        frameConfirm = super().createFrame(frameMain)
        frameConfirm.pack(side="right", padx=10, pady=40, fill=tk.X)
        buttonConfirm = super().createButton(master=frameConfirm, text="CONFIRMER ROBOT", cmd=lambda:self.followingFrame())
        buttonConfirm["bg"] = "darkblue"
        buttonConfirm["fg"] = "white"
        buttonConfirm["bd"] = tkUtils.ratioWidth(0.01, root)
        buttonConfirm["width"] = tkUtils.ratioWidth(0.06, root)
        buttonConfirm["height"] = tkUtils.ratioHeight(0.001, root)
        buttonConfirm["activebackground"] = "blue"
        buttonConfirm["activeforeground"] = "lightgrey"
        buttonConfirm.pack(fill = tk.X)
        #

        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FCreateRobot, self).reopenLastFrame())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)
        #

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
