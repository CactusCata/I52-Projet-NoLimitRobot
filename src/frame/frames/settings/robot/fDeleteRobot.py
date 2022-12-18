import frame.rootManager as rootManager
import robot.robotManager as robotManager

from frame.iFrame import IFrame

from tkinter import messagebox

class FDeleteRobot(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):
        root = rootManager.getRoot()

        # Nom du robot
        textName = super().createLabel(text="Nom du robot:")
        textName.pack()
        self.comboboxName = super().createComboBox(list=robotManager.getLoadedRobots())
        self.comboboxName.pack()

        confirmButton = super().createButton(text="Supprimer", cmd=lambda:self.confirmButtonAction())
        confirmButton.pack()

        buttonHelp = super().createButton(text="Aide")
        buttonHelp.pack()

        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FDeleteRobot, self).reopenLastFrame())
        buttonBack.pack()

    def confirmButtonAction(self):
        selectedRobotName = self.comboboxName.get()

        messagebox.showinfo(title="Information", message=f"Le robot {selectedRobotName} a bien été supprimé")
        robotManager.deleteRobot(selectedRobotName)

        super(FDeleteRobot, self).reopenLastFrame()