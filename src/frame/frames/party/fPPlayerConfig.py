import frame.rootManager as rootManager
import robot.robotManager as robotManager
import player.playerManager as playerManager
import utils.otherUtils as otherUtils

from robot.robotFile import RobotFile
from robot.robotChooser import RobotChooser

from frame.frames.party.fPPartyConfig import FPPartyConfig
from frame.messagesHelp import HELP_FPPLAYERCONFIG

import utils.tkinter.tkUtils as tkUtils

from frame.iFrame import IFrame

MIN_PLAYER_AMOUNT = 2
MAX_PLAYER_AMOUNT = 6

class FPPlayerConfig(IFrame):
    """
    Interface permetant à l'utilisateur de choisir
    des robots qui s'affronteront
    """

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FPPLAYERCONFIG)

        # Est-ce qu'un robot a été sélectionné
        self.selectedRobot = False

    def draw(self):

        root = rootManager.getRoot()
        robotsNames = robotManager.getLoadedRobots()

        super().createButtonHelp()

        # Remet à zero la liste des joueurs
        playerManager.initPlayerList()

        # Charge la liste des robots disponibles
        robotsFile = []
        for robotName in robotsNames:
            robotsFile.append(RobotFile(robotName))

        # Retour
        buttonBack = super().createButton(text="Retour", cmd=lambda:super(FPPlayerConfig, self).reopenLastFrame())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

        self.buttonNext = super().createButton(text="Suivant", cmd=lambda: rootManager.runNewFrame(FPPartyConfig(self)))
        self.buttonNext["state"] = "disabled"
        self.buttonNext.pack(side="bottom", anchor="se", pady=10, padx=10)

        frameRobotSelection = super().createFrame()
        frameRobotSelection.pack(side="left", ipadx=tkUtils.ratioWidth(0.04, root))
        # Canvas qui contient la liste des robots choisissables
        self.canvas = super().createCanvas(master=frameRobotSelection, width=tkUtils.ratioWidth(0.4, root), height=tkUtils.ratioHeight(0.4, root))
        self.canvas.pack()


        framePlayerSection = super().createFrame()
        framePlayerSection.pack(side="right", ipadx=40)

        # canvas et textes des robots-joueurs
        self.canvasPlayerList = []
        self.labelPlayerList = []
        for i in range(6):
            currentCanvasPlayer = super().createCanvas(master=framePlayerSection, width=playerManager.PLAYER_ICON_DIMENSIONS[0] + 2, height=playerManager.PLAYER_ICON_DIMENSIONS[1] + 2)
            currentCanvasPlayer.pack()
            self.canvasPlayerList.append(currentCanvasPlayer)
            currentLabelPlayer = super().createLabel(master=framePlayerSection, text=f"Joueur {i + 1}")
            currentLabelPlayer.pack()
            self.labelPlayerList.append(currentLabelPlayer)

        # Grille de sélection des robots
        self.robotChooser = RobotChooser(self.canvas, robotsFile)
        self.robotChooser.drawGrid()
        self.robotChooser.drawRobots()

        self.canvas.bind("<Motion>", lambda event:self.moveMouse(event.x, event.y))
        self.canvas.bind("<Button-1>", lambda event:self.clickEvent(event.x, event.y))

        # id du robot sous le curseur
        self.robotSelectedID = -1

        self.playerRobotCursor = 0

        self.buttonConfirmRobot = super().createButton(text="Confirmer robot", cmd=lambda: self.confirmRobot())
        self.buttonConfirmRobot.pack()



    def clickEvent(self, x, y):
        """
        Evènement déclanché lorsque un joueur clic
        dans dans le canvas de sélection des robots
        """
        id = self.robotSelectedID
        if (id == -1):
            return

        robotFile = self.robotChooser.getRobotFile(id)

        if (robotFile == None):
            return

        # Plus de place disponible
        if (self.playerRobotCursor >= MAX_PLAYER_AMOUNT):
            return

        # Si c'est la première selection de robot pour le
        # joueur, alors, on ajoute le joueur
        # Sinon on met à jour son robot
        if (len(playerManager.PLAYER_LIST) <= self.playerRobotCursor):
            playerManager.addPlayer(robotFile)
        else:
            playerManager.updatePlayer(robotFile, self.playerRobotCursor)

        # On déssine l'icon du robot dans la case du joueur
        player = playerManager.getPlayer(self.playerRobotCursor)
        logoPlayer = player.getRobotIconTk()
        currentCanvas = self.canvasPlayerList[self.playerRobotCursor]
        currentCanvas.create_image((playerManager.PLAYER_ICON_DIMENSIONS[0] // 2) + 3, (playerManager.PLAYER_ICON_DIMENSIONS[1] // 2) + 3, image=logoPlayer)
        currentLabel = self.labelPlayerList[self.playerRobotCursor]
        currentLabel["text"] = f"Joueur {self.playerRobotCursor + 1} : {player.getRobotFile().get_name()}"
        self.selectedRobot = True

    def confirmRobot(self):
        """
        Fonction appelée lorsque un robot est confirmé
        par un joueur
        """

        # Pas de confirmation possible si tous les
        # joueurs ont déjà un robot
        if (self.playerRobotCursor >= MAX_PLAYER_AMOUNT):
            return

        # On annule si aucun robot n'a été sélectionné
        if not self.selectedRobot:
            return

        # On met en vert le nom du joueur pour lui prouver la
        # réussite de sa confirmation
        self.labelPlayerList[self.playerRobotCursor]["fg"] = "#00FF00"

        playerManager.getPlayer(self.playerRobotCursor)

        self.playerRobotCursor += 1

        if (self.playerRobotCursor >= MIN_PLAYER_AMOUNT):
            self.buttonNext["state"] = "normal"

        self.selectedRobot = False


    def moveMouse(self, x, y):
        """
        Fonction appelé lorsque l'utilisateur bouge la souris.
        Permet de mettre en valeur le choix du robot du joueur.
        """

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
