from tkinter.filedialog import askopenfile
from shutil import copyfile
from pathlib import Path

import frame.rootManager as rootManager
from frame.frames.settings.robot.fEditRobot import FEditRobot
from robot.robotManager import *

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
        textDescription = super().createLabel(DescOptionnal, "(Optionnel) Description :\t")
        textDescription.pack(side="left")
        textboxDescription = super().createTextBox(DescOptionnal,"",width = 50, height = 20)
        textboxDescription.pack(side="right")

        PathOptionnal = super().createFrame(root) #choix optionnel
        PathOptionnal.pack()
        textPath = super().createLabel(PathOptionnal, "(Optionnel) Logo :\t")
        textPath.pack(side="left")
        buttonPath = super().createButton(PathOptionnal,text="Sélectionner votre Logo", cmd=lambda:self.selecPath(textboxName)) #filedialog.askopenfile(mode='r')
        buttonPath.pack(side="right")

        buttonConfirm = super().createButton(text="Confirmer", cmd=lambda:self.followingFrame(root, textboxName, textboxDescription))
        buttonConfirm.pack()

        buttonHelp = super().createButton(text="Aide")
        buttonHelp.pack()

        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FCreateRobot, self).reopenLastFrame())
        buttonBack.pack()



    def selecPath(self, boxname): #NOTE PERSO : Gérer la photo de base pour robot sans logo ajouté
        """
        Demande à l'utilisateur une image pour la copier coller dans le répertoire des
        images de robots, afin d'avoir une trace permanente des images des robots.
        L'image en .png possède le même nom que le répertoire de ce dit robot.
        """
        original = askopenfile(mode='r')
        robotname = boxname.get("1.0","end")
        robotname = uglynametorealname(robotname)
        new_one = f"../res/img/robot/" + robotname + ".png" #Chemin depuis le main !!!
        copyfile(original.name, new_one)

    def getFileName(self, charstar):
        """
        Extrait le nom du fichier avec son extension, depuis le chemin absolu.
        """
        file = ""
        i = -1
        while charstar[i] != '/':
            file += charstar[i]
            i -= 1
        realfile = file[::-1]
        return realfile

    def followingFrame(self, root, stringName, stringDesc):
        """ S'occupe de passer à la prochaine fenêtre ou non, en fonction des
        différentes erreurs présentes
        """
        filename = stringName.get("1.0", "end")
        description = stringDesc.get("1.0", "end")
        if len(filename) != 1: #taille nulle
            createNewRobot(filename, description)
            rootManager.runNewFrame(FEditRobot(self))

        else:
            labelerror = super().createLabel(root, "Vous n'avez pas donné de nom à votre robot ! (/OxO)/ (vous)", 30)
            labelerror["fg"] = "#FA0000"
            labelerror.pack()
            labelerror.after(5000, lambda:self.error(root, labelerror))

    def error(self, root, widget): #Erreur si l'utilisateur n'a pas mit de nom

        widget.destroy()
