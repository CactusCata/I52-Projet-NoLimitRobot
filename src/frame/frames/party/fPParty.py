import frame.rootManager as rootManager
import player.playerManager as playerManager
import utils.otherUtils as otherUtils
from time import time
from player.playerManager import PLAYER_ICON_DIMENSIONS
import utils.tkinter.tkUtils as tkUtils

from frame.messagesHelp import HELP_FPPARTY
from map.mapDrawer import MapDrawer
from frame.iFrame import IFrame
from game.game import Game

DEFAULT_MS_BETWEEN_TWO_ROBOT_ACTION = 200

class FPParty(IFrame):

    def __init__(self, previousFrame, map):
        super().__init__(previousFrame, HELP_FPPARTY)

        self.map = map
        self.root = rootManager.getRoot()

        self.playersHealthBar = []
        self.lastTaskID = -1

        self.speedGame = DEFAULT_MS_BETWEEN_TWO_ROBOT_ACTION
        self.gameIsStopped = False

    def draw(self):

        super().createButtonHelp()

        framePlayersStats = super().createFrame()
        framePlayersStats.pack(side="left", padx=tkUtils.ratioWidth(0.01, self.root))

        for player in playerManager.PLAYER_LIST:
            playerFrame = super().createFrame(master=framePlayersStats)
            playerFrame.pack(side="top")

            labelPlayerName = super().createLabel(master=playerFrame, text=player.getRobotFile().get_name())
            labelPlayerName.pack()

            canvasPlayerIcon = super().createCanvas(master=playerFrame, width=PLAYER_ICON_DIMENSIONS[0], height=PLAYER_ICON_DIMENSIONS[1])
            canvasPlayerIcon.create_image((PLAYER_ICON_DIMENSIONS[0] // 2) + 1, (PLAYER_ICON_DIMENSIONS[1] // 2) + 1, image=player.getRobotIconTk())
            canvasPlayerIcon.pack()

            canvasPlayerHealth = super().createCanvas(master=playerFrame, width=100, height=30)
            canvasPlayerHealth.create_rectangle(0, 0, 100, 30, fill="black")
            canvasPlayerHealth.create_rectangle(5, 5, 95, 25, fill=otherUtils.convertHealthPercentToColor(100))
            canvasPlayerHealth.pack()
            self.playersHealthBar.append(canvasPlayerHealth)


        # Map
        self.canvasMap = super().createCanvas(width=700, height=500)
        self.canvasMap.pack(side="left", padx=tkUtils.ratioWidth(0.01, self.root))
        self.mapDrawer = MapDrawer(self.canvasMap, self.map, playerManager.PLAYER_LIST)
        self.mapDrawer.clear()
        self.mapDrawer.drawMap()
        self.mapDrawer.drawGrid()
        self.mapDrawer.drawRobot()
        self.mapDrawer.drawMine()
        self.game = Game(map=self.map)

        # game speed
        frameGameSpeed = super().createFrame()
        frameGameSpeed.pack(side="left", padx=tkUtils.ratioWidth(0.01, self.root))
        labelGameSpeed = super().createLabel(master=frameGameSpeed, text="Vitesse du jeu")
        labelGameSpeed.pack(side="top")
        self.scalebarSpeedGame = super().createScalebar(master=frameGameSpeed, orientation="vertical", from_=0, to=500, defaultValue=300, length=500, tickInterval=10, callback= lambda event: self.speedGameChanged())
        self.scalebarSpeedGame.pack(side="top")

        # Continuer
        self.buttonContinue = super().createButton(text="Continuer", cmd=lambda:self.goToTheNextFrame())
        self.buttonContinue["state"] = "disabled"
        self.buttonContinue.pack()

        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:self.tryReopenLastFrame())
        buttonBack.pack(side="bottom")

        self.lastTaskID = self.root.after(self.speedGame, self.nextPartyStep)

    def goToTheNextFrame(self):
        rootManager.runNewFrame(FPEndParty(self, self.game.getWinner()))

    def nextPartyStep(self):
        if (self.game.isEnded()):
            self.buttonContinue["state"] = "normal"
            return

        if (self.gameIsStopped):
            return

        start = time()
        self.game.next()

        for i in range(len(playerManager.PLAYER_LIST)):
            player = playerManager.PLAYER_LIST[i]
            robotHealthPercent = 100 * player.getRobotParty().get_energy() // player.getRobotParty().get_max_energy()
            canvasPlayerHealth = self.playersHealthBar[i]
            canvasPlayerHealth.delete("all")
            canvasPlayerHealth.create_rectangle(0, 0, 100, 30, fill="black")
            canvasPlayerHealth.create_rectangle(5, 5, 95, 25, fill="white")
            canvasPlayerHealth.create_rectangle(5, 5, 5 + (robotHealthPercent * 90) / 100, 25, fill=otherUtils.convertHealthPercentToColor(robotHealthPercent))


        self.mapDrawer.clear()
        self.mapDrawer.drawMap()
        self.mapDrawer.drawGrid()
        self.mapDrawer.drawRobot()
        self.mapDrawer.drawMine()

        totalTime = int((time() - start) * 1000)
        timeToWait = max(0, self.speedGame - totalTime)

        self.lastTaskID = self.root.after(timeToWait, self.nextPartyStep)

    def tryReopenLastFrame(self):
        for player in playerManager.PLAYER_LIST:
            player.getRobotParty().reset_energy()

        self.map.removeData()
        self.root.after_cancel(self.lastTaskID)
        super(FPParty, self).reopenLastFrame()

    def speedGameChanged(self):
        scalebarValue = int(self.scalebarSpeedGame.get())
        if (scalebarValue == 0):
            self.root.after_cancel(self.lastTaskID)
            self.gameIsStopped = True
        else:
            self.speedGame = int(510 - self.scalebarSpeedGame.get())
            if (self.gameIsStopped):
                self.gameIsStopped = False
                self.nextPartyStep()
