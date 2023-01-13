import frame.rootManager as rootManager
import robot.robotManager as robotManager

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FDELETEROBOT


import tkinter as tk
from tkinter import messagebox
import utils.tkinter.tkUtils as tkUtils

class FDeleteRobot(IFrame):
    """
    Propose à l'utilisateur de supprimer un robot
    """

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FDELETEROBOT)

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        labelTitle = super().createLabel(master=root, text="Suppression de robot", fontSize=30)
        labelTitle.pack(side="top")

        frameMain = super().createFrame(root)
        frameMain.pack(pady=tkUtils.ratioHeight(0.04, root))

        # Nom du robot
        textName = super().createLabel(master=frameMain, text="Nom du robot:")
        textName.pack(anchor="n")

        # Liste de nom des robots
        self.comboboxName = super().createComboBox(list=robotManager.getLoadedRobots())
        self.comboboxName.pack(anchor="n")

        # Confirm
        buttonConfirm = super().createButton(text="Supprimer", cmd=lambda:self.confirmButtonAction())
        buttonConfirm.pack(pady=tkUtils.ratioHeight(0.01, root))

        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FDeleteRobot, self).reopenLastFrame())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

    def confirmButtonAction(self):
        """
        Méthode appelée lorsque l'utilisateur lorsqu'il appuie
        sur le bouton de confirmation de suppression d'un robot
        """
        selectedRobotName = self.comboboxName.get()

        # Ne rien faire si aucun robot entré
        if (selectedRobotName == ""):
            return

        messagebox.showinfo(title="Information", message=f"Le robot {selectedRobotName} a bien été supprimé")
        robotManager.deleteRobot(selectedRobotName)

        super(FDeleteRobot, self).reopenLastFrame()
