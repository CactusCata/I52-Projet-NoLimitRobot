import frame.rootManager as rootManager
import robot.robotManager as robotManager

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FDELETEROBOT


import tkinter as tk
from tkinter import messagebox
import utils.tkinter.tkUtils as tkUtils

class FDeleteRobot(IFrame):

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

        self.comboboxName = super().createComboBox(list=robotManager.getLoadedRobots())
        self.comboboxName.pack(anchor="n")

        buttonConfirm = super().createButton(text="Supprimer", cmd=lambda:self.confirmButtonAction())
        buttonConfirm.pack(pady=tkUtils.ratioHeight(0.01, root))

        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FDeleteRobot, self).reopenLastFrame())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

    def confirmButtonAction(self):
        selectedRobotName = self.comboboxName.get()

        messagebox.showinfo(title="Information", message=f"Le robot {selectedRobotName} a bien été supprimé")
        robotManager.deleteRobot(selectedRobotName)

        super(FDeleteRobot, self).reopenLastFrame()
