import frame.rootManager as rootManager
import robot.robotManager as robotManager
import player.playerManager as playerManager
import utils.otherUtils as otherUtils

from robot.robotFile import RobotFile
from robot.robotChooser import RobotChooser

from frame.frames.party.fPPartyConfig import FPPartyConfig

import utils.tkinter.tkUtils as tkUtils

from frame.iFrame import IFrame

MIN_PLAYER_AMOUNT = 2
MAX_PLAYER_AMOUNT = 6

class FPPlayerConfig(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

        self.selectedRobot = False

    def draw(self):

        robotsNames = robotManager.getLoadedRobots()

        # Remet à zero la liste des joueurs
        playerManager.initPlayerList()

        robotsFile = []
        for robotName in robotsNames:
            robotsFile.append(RobotFile(robotName))

        frameRobotSelection = super().createFrame()
        frameRobotSelection.pack(side="left", ipadx=40)
        # Canvas qui contient la liste des robots choisissables
        self.canvas = super().createCanvas(master=frameRobotSelection, width=300, height=300)
        self.canvas.pack()

        
        framePlayerSection = super().createFrame()
        framePlayerSection.pack(side="right", ipadx=40)
        # canvas et textes des robots-joueurs
        self.canvasPlayerList = []
        self.labelPlayerList = []
        for i in range(6):
            currentCanvasPlayer = super().createCanvas(master=framePlayerSection, width=30, height=30)
            currentCanvasPlayer.pack()
            self.canvasPlayerList.append(currentCanvasPlayer)
            currentLabelPlayer = super().createLabel(master=framePlayerSection, text=f"Joueur {i}")
            currentLabelPlayer.pack()
            self.labelPlayerList.append(currentLabelPlayer)

        self.robotChooser = RobotChooser(self.canvas, robotsFile, xPas=42, yPas=42, imageDimension=(40,40))
        self.robotChooser.drawGrid()
        self.robotChooser.drawRobots()

        self.canvas.bind("<Motion>", lambda event:self.moveMouse(event.x, event.y))
        self.canvas.bind("<Button-1>", lambda event:self.clickEvent(event.x, event.y))

        # id du robot sous le curseur
        self.robotSelectedID = -1

        self.playerRobotCursor = 0

        self.buttonConfirmRobot = super().createButton(text="Confirmer robot", cmd=lambda: self.confirmRobot())
        self.buttonConfirmRobot.pack()

        self.buttonNext = super().createButton(text="Suivant", cmd=lambda: rootManager.runNewFrame(FPPartyConfig(self)))
        self.buttonNext["state"] = "disabled"
        self.buttonNext.pack()

        # Aide
        buttonHelp = super().createButtonHelp(msg="aide")
        buttonHelp.pack()

        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FPPlayerConfig, self).reopenLastFrame())
        buttonBack.pack()

    def clickEvent(self, x, y):
        id = self.robotSelectedID
        if (id == -1):
            return 

        robotFile = self.robotChooser.getRobotFile(id)

        if (robotFile == None):
            return

        # Plus de place disponible
        if (self.playerRobotCursor >= MAX_PLAYER_AMOUNT):
            return

        if (len(playerManager.PLAYER_LIST) <= self.playerRobotCursor):
            playerManager.addPlayer(robotFile)
        else:
            playerManager.updatePlayer(robotFile, self.playerRobotCursor)

        player = playerManager.getPlayer(self.playerRobotCursor)
        logoPlayer = player.getIconTk()
        currentCanvas = self.canvasPlayerList[self.playerRobotCursor]
        currentCanvas.create_image(20, 20, image=logoPlayer)
        currentLabel = self.labelPlayerList[self.playerRobotCursor]
        currentLabel["text"] = f"Joueur {self.playerRobotCursor + 1} : {player.getRobotFile().get_name()}"
        self.selectedRobot = True
    
    def confirmRobot(self):

        if (self.playerRobotCursor >= MAX_PLAYER_AMOUNT):
            return

        if not self.selectedRobot:
            return

        self.labelPlayerList[self.playerRobotCursor]["fg"] = "#00FF00"

        playerManager.getPlayer(self.playerRobotCursor)

        self.playerRobotCursor += 1
        
        if (self.playerRobotCursor >= 3):
            self.buttonNext["state"] = "normal"

        self.selectedRobot = False

        
    def moveMouse(self, x, y):
        
        ids = self.canvas.find_withtag("current")

        # Ne pas traiter le cas où il n'y a pas d'élément à inspecter
        if (len(ids) == 0):
            if (self.robotSelectedID != -1):
                self.canvas.move(self.robotSelectedID, -5, -5)
            self.robotSelectedID = -1
            return

        id = ids[0]
        tag = tkUtils.itemHasTag(self.canvas, id, tkUtils.startWithFunction, "robot")

        if (tag == None):
            return None

        if (id != self.robotSelectedID):
            self.canvas.move(id, 5, 5)
            self.canvas.move(self.robotSelectedID, -5, -5)
            self.robotSelectedID = id