import frame.rootManager as rootManager
import robot.robotManager as robotManager

from robot.robotFile import RobotFile
from robot.robotChooser import RobotChooser

from frame.frames.party.fPPartyConfig import FPPartyConfig

from frame.iFrame import IFrame

MAX_PLAYER_AMOUNT = 6

class FPPlayerConfig(IFrame):

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

    def draw(self):

        robotsNames = robotManager.getLoadedRobots()
        print(f"Loaded robots: {robotsNames}")

        robotsFile = []
        for robotName in robotsNames:
            robotsFile.append(RobotFile(robotName))

        # Canvas qui contient la liste des robots choisissables
        self.canvas = super().createCanvas(width=300, height=300)
        self.canvas.pack()

        self.robotChooser = RobotChooser(self.canvas, robotsFile)
        self.robotChooser.drawGrid()
        self.robotChooser.drawRobots()

        self.canvas.bind("<Motion>", lambda event:self.moveMouse(event.x, event.y))
        self.canvas.bind("<Button-1>", lambda event:self.clickEvent(event.x, event.y))

        # Association entre un joueur numero i correspondant
        # à l'indice dans la liste playersRobot et son robotFile    
        self.playersRobot = [None] * MAX_PLAYER_AMOUNT
        self.playerRobotCursor = 0

        # id du robot sous le curseur
        self.robotSelectedID = -1

        self.buttonConfirmRobot = super().createButton(text="Confirmer robot", cmd=lambda event: self.confirmRobot(event))
        self.buttonConfirmRobot.pack()

        self.buttonNext = super().createButton(text="Suivant", cmd=lambda: rootManager.runNewFrame(FPPartyConfig(self)))
        self.buttonNext["state"] = "disabled"
        self.buttonNext.pack()

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

        self.playersRobot[self.playerRobotCursor] = robotFile
    
    def confirmRobot(self, event):

        if (self.playerRobotCursor >= MAX_PLAYER_AMOUNT):
            return

        self.canvas.create_text(20 * self.playerRobotCursor, 280, text=f"player {self.playerRobotCursor + 1}")
        self.canvas.create_image(20 * self.playerRobotCursor, 250, image=self.playersRobot[self.playerRobotCursor])

        self.playerRobotCursor += 1
        
        if (self.playerRobotCursor >= 3):
            self.buttonNext["state"] = "normal"


        
    def moveMouse(self, x, y):
        
        ids = self.canvas.find_withtag("current")

        # Ne pas traiter le cas où il n'y a pas d'élément à inspecter
        if (len(ids) == 0):
            self.robotSelectedID = -1
            return

        id = ids[0]
        if (id != self.robotSelectedID):
            self.canvas.move(id, 5, 5)
            self.canvas.move(self.robotSelectedID, -5, -5)
            self.robotSelectedID = id