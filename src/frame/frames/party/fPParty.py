import frame.rootManager as rootManager
import game.gameManager as gameManager
import player.playerManager as playerManager
import utils.otherUtils as otherUtils
import utils.mapUtils as mapUtils
from time import time

from map.mapDrawer import MapDrawer
from frame.iFrame import IFrame
from game.game import Game

MS_BETWEEN_TWO_ROBOT_ACTION = 200

class FPParty(IFrame):

    def __init__(self, previousFrame, map):
        super().__init__(previousFrame, "AIDE")

        self.map = map
        self.root = rootManager.getRoot()

        self.playersHealthBar = []
        self.lastTaskID = -1

    def draw(self):

        super().createButtonHelp()

        framePlayersStats = super().createFrame()
        framePlayersStats.pack(side="left")

        for player in playerManager.PLAYER_LIST:
            playerFrame = super().createFrame(master=framePlayersStats)
            playerFrame.pack(side="top")

            labelPlayerName = super().createLabel(master=playerFrame, text=player.getRobotFile().get_name())
            labelPlayerName.pack()
            
            canvasPlayerIcon = super().createCanvas(master=playerFrame, width=50, height=50)
            canvasPlayerIcon.create_image(10, 10, image=player.getIconTk())
            canvasPlayerIcon.pack()

            canvasPlayerHealth = super().createCanvas(master=playerFrame, width=100, height=30)
            canvasPlayerHealth.create_rectangle(0, 0, 100, 30, fill="black")
            canvasPlayerHealth.create_rectangle(5, 5, 95, 25, fill=otherUtils.convertHealthPercentToColor(100))
            canvasPlayerHealth.pack()
            self.playersHealthBar.append(canvasPlayerHealth)

        path = mapUtils.getPath(self.map, (1, 0), (1, 12))
        print(path)

        # Map
        self.canvasMap = super().createCanvas(width=700, height=500)
        self.canvasMap.pack()
        self.mapDrawer = MapDrawer(self.canvasMap, self.map, playerManager.PLAYER_LIST)
        self.mapDrawer.clear()
        self.mapDrawer.drawMap()
        self.mapDrawer.drawGrid()
        self.mapDrawer.drawRobot()
        self.game = Game(map=self.map)

        self.lastTaskID = self.root.after(MS_BETWEEN_TWO_ROBOT_ACTION, self.nextPartyStep)


    def nextPartyStep(self):
        if (self.game.isEnded()):
            print("THE GAME IS ENDED")
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

        totalTime = int((time() - start) * 1000)
        timeToWait = max(0, MS_BETWEEN_TWO_ROBOT_ACTION - totalTime)

        self.lastTaskID = self.root.after(timeToWait, self.nextPartyStep)