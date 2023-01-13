import frame.rootManager as rootManager
import player.playerManager as playerManager
import utils.otherUtils as otherUtils
from time import time
from player.playerManager import PLAYER_ICON_DIMENSIONS
import utils.tkinter.tkUtils as tkUtils

from frame.frames.party.fPEndParty import FPEndParty

from frame.messagesHelp import HELP_FPPARTY
from map.mapDrawer import MapDrawer
from frame.iFrame import IFrame
from game.game import Game

DEFAULT_MS_BETWEEN_TWO_ROBOT_ACTION = 200

class FPParty(IFrame):
    """
    Permet à l'utilisateur de visualiser la partie ainsi
    que les actions réalisées par les robots.
    A la fin de la partie, l'utilisateur peut voir qui a gagné.
    """

    def __init__(self, previousFrame, map):
        super().__init__(previousFrame, HELP_FPPARTY)

        self.root = rootManager.getRoot()

        # Carte utilisée
        self.map = map

        # Liste qui contient les canvas des barres
        # de vie des joueurs
        self.playersHealthBar = []

        # ID de la task en cours
        self.lastTaskID = -1

        # Temps entre deux actions de robot
        self.speedGame = DEFAULT_MS_BETWEEN_TWO_ROBOT_ACTION

        # Si la vitesse du jeu est mise à 0
        self.gameIsStopped = False

    def draw(self):

        super().createButtonHelp()

        framePlayersStats = super().createFrame()
        framePlayersStats.pack(side="left", padx=tkUtils.ratioWidth(0.01, self.root))

        # Pour chaque joueur, on affiche le nom, l'icon et la vie de son robot
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


        # Dessin de la carte
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
        """
        Méthode executée lorsque l'utilisateur souhaite aller
        à l'écran des résultats de la partie
        """
        rootManager.runNewFrame(FPEndParty(self, self.game.getWinner()))

    def nextPartyStep(self):
        """
        Execute l'action du prochain robot tant que la partie
        n'est pas terminée.
        Si la partie est terminée, on débloque le bouton
        "Continuer"
        """

        # Si la partie est termiée, on débloque le bouton continuer
        if (self.game.isEnded()):
            self.buttonContinue["state"] = "normal"
            return

        if (self.gameIsStopped):
            return

        start = time()
        self.game.next()

        # On re-déssine la vie des robots
        for i in range(len(playerManager.PLAYER_LIST)):
            player = playerManager.PLAYER_LIST[i]
            robotHealthPercent = 100 * player.getRobotParty().get_energy() // player.getRobotParty().get_max_energy()
            canvasPlayerHealth = self.playersHealthBar[i]
            canvasPlayerHealth.delete("all")
            canvasPlayerHealth.create_rectangle(0, 0, 100, 30, fill="black")
            canvasPlayerHealth.create_rectangle(5, 5, 95, 25, fill="white")
            canvasPlayerHealth.create_rectangle(5, 5, 5 + (robotHealthPercent * 90) / 100, 25, fill=otherUtils.convertHealthPercentToColor(robotHealthPercent))


        # On re-déssine la carte, la grille, les robots et les mines
        self.mapDrawer.clear()
        self.mapDrawer.drawMap()
        self.mapDrawer.drawGrid()
        self.mapDrawer.drawRobot()
        self.mapDrawer.drawMine()

        # On soustrait au temps entre deux instuctions de robot le temps
        # d'execution de notre fonction. Permet d'avoir un fonctionnement
        # plus vrai
        totalTime = int((time() - start) * 1000)
        timeToWait = max(20, self.speedGame - totalTime)

        self.lastTaskID = self.root.after(timeToWait, self.nextPartyStep)

    def tryReopenLastFrame(self):
        """
        Fonction executée lorsque l'utilisateur appuie sur le bouton
        de retour
        """

        # On remet la vie de chacun des robots
        for player in playerManager.PLAYER_LIST:
            player.getRobotParty().reset_energy()
        
        self.map.removeData()

        # On annule la task courante
        self.root.after_cancel(self.lastTaskID)

        super(FPParty, self).reopenLastFrame()

    def speedGameChanged(self):
        """
        Evenement déclanché lorsque l'utilisateur manipule
        la scalebar de vitesse du jeu
        """

        scalebarValue = int(self.scalebarSpeedGame.get())

        if (scalebarValue == 0): # Si la vitesse vaut 0, alors on met le jeu en pause
            self.root.after_cancel(self.lastTaskID)
            self.gameIsStopped = True
        else: # Sinon mettre la vitesse demandée en place
            self.speedGame = int(510 - self.scalebarSpeedGame.get())
            if (self.gameIsStopped):
                self.gameIsStopped = False
                self.nextPartyStep()
