import frame.rootManager as rootManager
import robot.robotManager as robotManager
import utils.instructionUtils as instructionUtils
import instruction.instructionAnalyser as instructionAnalyser

from frame.iFrame import IFrame
from frame.messagesHelp import HELP_FEDITROBOT
from robot.robotFile import RobotFile
from utils.tkinter.tkPerformer import TkPerformer

import player.playerManager as playerManager

from tkinter import Scrollbar

class FEditRobot(IFrame):
    """
    Propose d'éditer un robot
    """

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FEDITROBOT)

        # Fichier du robot en cours d'édition
        self.currentRobotFile = None

        # Est-ce que des changements ont eu lieu
        self.currentRobotHasChanged = False

    def draw(self):
        root = rootManager.getRoot()

        super().createButtonHelp()

        frameRobot = super().createFrame()
        frameRobot.pack(side="left", ipadx=int(0.1 * root.winfo_width()))

        # Nom du robot
        textName = super().createLabel(master=frameRobot, text="Nom du robot:")
        textName.pack()
        self.comboboxName = super().createComboBox(master=frameRobot, list=robotManager.getLoadedRobots(), callback=lambda event: self.selectRobot(event))
        self.comboboxName.pack()

        # Logo
        self.canvasLogo = super().createCanvas(master=frameRobot, width=playerManager.PLAYER_ICON_DIMENSIONS[0] + 2, height=playerManager.PLAYER_ICON_DIMENSIONS[1] + 2)
        self.canvasLogo.pack()

        # Description
        textDescription = super().createLabel(master=frameRobot, text="(Optionnel) Description :")
        textDescription.pack()
        self.entryDescription = super().createEntry(master=frameRobot, width=50)
        self.entryDescription.bind('<KeyRelease>', lambda event: self.writeInTextBox(event))
        self.entryDescription.pack()

        # Instruction
        instructLabelInfo = super().createLabel(master=frameRobot, text="Instructions")
        instructLabelInfo.pack()

        instructFrame = super().createFrame(master=frameRobot)
        instructFrame.pack()

        #instructValidatorLabel = super().createLabel(text="Instructions valides", fg="00FF00")
        #instructValidatorLabel.pack()

        instructScrollbar = Scrollbar(instructFrame)
        instructScrollbar.pack(side="right", fill="y")

        self.instructTextBox = super().createTextBox(instructFrame, width=30, height=10)
        self.instructTextBox.configure(yscrollcommand=instructScrollbar.set)
        self.instructTextBox.bind('<KeyRelease>', lambda event: self.writeInTextBox(event))
        self.instructTextBox.pack(side="left", fill="y")

        instructScrollbar.configure(command=self.instructTextBox.yview)
        self.instructTextBox.pack()

        # Confirmer
        self.buttonSave = super().createButton(master=frameRobot, text="Sauvegarder", cmd=lambda:self.saveRobotConfig())
        self.buttonSave["state"] = "disabled"
        self.buttonSave.pack()

        # Retour
        buttonBack = super().createButton(master=frameRobot, text="Retour", cmd=lambda:self.tryToReopenLastFrame())
        buttonBack.pack()

        # Aide sur la programmation des robots
        frameHelpInstruct = super().createFrame()
        frameHelpInstruct.pack(side="right", ipadx=int(0.1 * root.winfo_width()))

        self.labelInstructError = super().createLabel(master=frameHelpInstruct)
        self.labelInstructError["wraplength"] = int(0.25 * root.winfo_width())
        self.labelInstructError.pack()

        labelHelpInstruct = super().createLabel(master=frameHelpInstruct, text="Aide sur les instructions")
        labelHelpInstruct.pack()

        # Dictionnaire des instructions
        self.comboboxHelpInstruct = super().createComboBox(master=frameHelpInstruct, list=list(instructionUtils.INSTRUCTION_LIST.keys()), callback=lambda event: self.selectInstructionEvent(event))
        self.comboboxHelpInstruct.pack()

        self.labelHelpInstruct = super().createLabel(master=frameHelpInstruct)
        self.labelHelpInstruct["wraplength"] = int(0.25 * root.winfo_width())
        self.labelHelpInstruct.pack()

    def selectRobot(self, event):
        """
        Evenement déclanché lorsque l'utilisateur sélectionne un nom de robot
        """

        # Nom du robot
        robotSelectedName = self.comboboxName.get()

        # Propose de sauvegarder l'état du robot s'il a été modifié
        if (self.currentRobotHasChanged and robotSelectedName != self.currentRobotFile.get_name()):
            returnCode = TkPerformer(rootManager.getRoot(), "Editeur de robot", "Voulez-vous sauvegarder les modifications ?").run()
            if (returnCode == 0):
                self.saveRobotConfig()
            elif (returnCode == 2):
                self.comboboxName.current(self.comboboxName.current())
                return

        # Chargement du fichier correspondant au robot
        self.currentRobotFile = RobotFile(robotSelectedName)

        # Mise a jour du logo
        self.currentRobotFile.load_icon()
        self.currentRobotFile.load_icon_tk()
        self.canvasLogo.delete("all")
        self.canvasLogo.create_image((playerManager.PLAYER_ICON_DIMENSIONS[0] // 2) + 1, (playerManager.PLAYER_ICON_DIMENSIONS[1] // 2) + 1, image=self.currentRobotFile.get_icon_tk())

        # Suppression du contenu des boite à texte
        self.entryDescription.delete(0,"end")
        self.instructTextBox.delete(1.0, "end")

        # Insertion des données du robot dans les boites à texte
        self.entryDescription.insert(0, self.currentRobotFile.get_desc())

        # Insertion des instructions du robot dans la boite à texte
        self.instructTextBox.insert(float(1), self.currentRobotFile.get_danger_instruction() + "\n")
        instructions = self.currentRobotFile.get_instr()
        if (len(instructions) > 0):
            for i in range(1, len(instructions)):
                self.instructTextBox.insert(float(i + 1), instructions[i - 1] + '\n')
            self.instructTextBox.insert(float(len(instructions) + 1), instructions[len(instructions) - 1])

    def saveRobotConfig(self):
        """
        Sauvegarde les changements du robot
        """
        robotName = self.currentRobotFile.get_name()
        robotDescription = self.entryDescription.get()
        robotInstructionText = self.instructTextBox.get("1.0", "end-1c")

        # Ne pas sauvegarder si le nombre d'instruction est
        # inférieur à 6
        if (len(robotInstructionText.split("\n")) < 6):
            self.labelHelpInstruct["text"] = "Au moins 6 instructions sont nécéssaires"
            return

        # Ne pas sauvegarder si le nombre d'instruction est
        # supérieur à 20
        if (len(robotInstructionText.split("\n")) > 20):
            self.labelHelpInstruct["text"] = "Vous avez trop d'instructions !"
            return

        # Si les instructions ne sont pas valides, annuler
        # et indiquer pourquoi
        instructionCorrect = instructionAnalyser.instructionsAreValide(robotInstructionText)
        if (instructionCorrect != instructionAnalyser.INSTRUCTION_CORRECT):
            self.labelInstructError["text"] = instructionCorrect
            return

        # Si pas d'erreur, retirer le dernier message
        # d'erreur s'il y en a un
        if (self.labelInstructError["text"] != ""):
            self.labelInstructError["text"] = ""

        # Mise à jour des instructions des robots
        robotInstructions = robotInstructionText.split('\n')
        robotManager.updateRobot(robotName, robotDescription, robotInstructions)
        self.buttonSave["state"] = "disabled"
        self.currentRobotHasChanged = False

    def writeInTextBox(self, event):
        """
        Evenement déclanché lorsque l'utilisateur écrit dans la zone de description.
        Propose alors la sauvegarde.
        """
        if (not self.currentRobotHasChanged):
            self.buttonSave["state"] = "normal"
            self.currentRobotHasChanged = True

    def tryToReopenLastFrame(self):
        """
        Propose à l'utilisateur de sauvegarder si une édition à eu lieu
        sans sauvegarde
        """

        if (self.currentRobotHasChanged):
            returnCode = TkPerformer(rootManager.getRoot(), "Editeur de robot", "Voulez-vous sauvegarder les modifications ?").run()
            if (returnCode == 0):
                self.saveRobotConfig()
            elif (returnCode == 1):
                return

        super(FEditRobot, self).reopenLastFrame()

    def selectInstructionEvent(self, event):
        """
        Informe l'utilisateur sur une instruction
        """
        indexInstruct = self.comboboxHelpInstruct.get()
        instruction = instructionUtils.INSTRUCTION_LIST[indexInstruct]

        self.labelHelpInstruct["text"] = instruction.getInfo()
