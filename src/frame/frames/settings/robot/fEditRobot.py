import frame.rootManager as rootManager
import robot.robotManager as robotManager
import utils.instructionUtils as instructionUtils
import instruction.instructionAnalyser as instructionAnalyser

from frame.iFrame import IFrame
from robot.robotFile import RobotFile
from utils.tkinter.tkPerformer import TkPerformer

from tkinter import Scrollbar

class FEditRobot(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

        self.currentRobotFile = None
        self.currentRobotHasChanged = False

    def draw(self):
        root = rootManager.getRoot()

        frameRobot = super().createFrame()
        frameRobot.pack(side="left", ipadx=int(0.1 * root.winfo_width()))

        # Nom du robot
        textName = super().createLabel(master=frameRobot, text="Nom du robot:")
        textName.pack()
        self.comboboxName = super().createComboBox(master=frameRobot, list=robotManager.getLoadedRobots(), callback=lambda event: self.selectRobot(event))
        self.comboboxName.pack()

        # Logo
        self.canvasLogo = super().createCanvas(master=frameRobot, width=100, height=100)
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

        # Aide
        buttonHelp = super().createButton(master=frameRobot, text="Aide")
        buttonHelp.pack()

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
        self.currentRobotFile.load_logo()
        self.canvasLogo.delete("all")
        self.canvasLogo.create_image(50, 50, image=self.currentRobotFile.get_logo())

        # Suppression du contenu des boite à texte
        self.entryDescription.delete(0,"end")
        self.instructTextBox.delete(1.0, "end")

        # Insertion des données du robot dans les boites à texte
        self.entryDescription.insert(0, self.currentRobotFile.get_desc())

        instructions = self.currentRobotFile.get_instr()
        if (len(instructions) > 0):
            for i in range(len(instructions) - 1):
                self.instructTextBox.insert(float(i + 1), instructions[i] + '\n')
            self.instructTextBox.insert(float(len(instructions)), instructions[len(instructions) - 1])
 
    def saveRobotConfig(self):
        """
        Sauvegarde les changements du robot
        """
        robotName = self.currentRobotFile.get_name()
        robotDescription = self.entryDescription.get()
        robotInstructionText = self.instructTextBox.get("1.0", "end-1c")

        instructionCorrect = instructionAnalyser.instructionsAreValide(robotInstructionText)
        if (instructionCorrect != instructionAnalyser.INSTRUCTION_CORRECT):
            self.labelInstructError["text"] = instructionCorrect
            return

        print("test:" + self.labelInstructError["text"])
        if (self.labelInstructError["text"] != ""):
            print("text has been updated")
            self.labelInstructError["text"] = ""
            
        robotInstructions = robotInstructionText.split('\n')
        robotManager.updateRobot(robotName, robotDescription, robotInstructions)
        self.buttonSave["state"] = "disabled"
        self.currentRobotHasChanged = False

    def writeInTextBox(self, event):
        """
        Evenement déclanché lorsque l'utilisateur écrit dans la zone de description
        """
        if (not self.currentRobotHasChanged):
            self.buttonSave["state"] = "normal"
            self.currentRobotHasChanged = True

    def tryToReopenLastFrame(self):

        if (self.currentRobotHasChanged):
            returnCode = TkPerformer(rootManager.getRoot(), "Editeur de robot", "Voulez-vous sauvegarder les modifications ?").run()
            if (returnCode == 0):
                self.saveRobotConfig()
            elif (returnCode == 1):
                return

        super(FEditRobot, self).reopenLastFrame()

    def selectInstructionEvent(self, event):
        indexInstruct = self.comboboxHelpInstruct.get()
        instruction = instructionUtils.INSTRUCTION_LIST[indexInstruct]

        self.labelHelpInstruct["text"] = instruction.getInfo()