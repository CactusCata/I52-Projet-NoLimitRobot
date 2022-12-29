import frame.rootManager as rootManager
import map.mapManager as mapManager
import game.gameManager as gameManager
import player.playerManager as playerManager

from map.mapDrawer import MapDrawer
import utils.mapUtils as mapUtils

from frame.iFrame import IFrame
from frame.frames.party.fPParty import FPParty

from tkinter import StringVar

class FPMapConfig(IFrame):
    """
    Menu déroulant avec la liste des noms de map
    canvas avec la visualisation de la map
    Radio button entre equidistance des robots et spreadplayer
    Si spreadPlayer, afficher un scalebar de distance minimale entre chaque robot
    Lancer la partie
    retour
    aide
    """

    def __init__(self, previousFrame):
        super().__init__(previousFrame)

        self.scalebarMinSpreadDistance = None
        self.map = None

    def draw(self):
        root = rootManager.getRoot()

        frameLeft = super().createFrame()
        frameLeft.pack(side="left", ipadx=50)

        self.frameLeftTop = super().createFrame(master=frameLeft)
        self.frameLeftTop.pack(side="top", ipady=50)
        frameLeftBot = super().createFrame(master=frameLeft)
        frameLeftBot.pack(side="bottom", ipady=50)

        frameRight = super().createFrame()
        frameRight.pack(side="right", ipadx=50)

        # Choix de la map
        labelMapName = super().createLabel(master=self.frameLeftTop, text="Choisir la map:")
        labelMapName.pack()
        self.comboBoxMapName = super().createComboBox(master=self.frameLeftTop, list=mapManager.getLoadedMaps(), callback=lambda event: self.mapSelectedChanged(event))
        self.comboBoxMapName.pack()

        # Map
        self.canvasMap = super().createCanvas(master=frameRight, width=700, height=500)
        self.canvasMap.pack()

        # Choix du placement des robots
        self.stringVarRadioButton = StringVar()
        self.stringVarRadioButton.set("equidistance")
        self.radioButtonEquidistance = super().createRadioButton(master=self.frameLeftTop, text="equidistance", serializedValue="EQUIDISTANCE", variable=self.stringVarRadioButton, callback=lambda: self.updateRadioButton())
        self.radioButtonEquidistance.select()
        self.radioButtonEquidistance.pack()
        self.radioButtonSpread = super().createRadioButton(master=self.frameLeftTop, text="spread robots", serializedValue="SPREAD_ROBOTS", variable=self.stringVarRadioButton, callback=lambda: self.updateRadioButton())
        self.radioButtonSpread.pack()

        # Confirmer
        buttonConfirm = super().createButton(master=frameLeftBot, text="Voir la partie", cmd=lambda:self.followingFrame())
        buttonConfirm.pack()

        # Aide
        buttonHelp = super().createButtonHelp(master=frameLeftBot, msg="aide")
        buttonHelp.pack()

        # Retour
        buttonBack = super().createButton(master=frameLeftBot, text="Retour", cmd=lambda:super(FPMapConfig, self).reopenLastFrame())
        buttonBack.pack()

    def mapSelectedChanged(self, event):
        """
        Evenement déclanché lorsque l'utilisateur choisi une carte
        """

        self.mapName = self.comboBoxMapName.get()

        # object map associé
        self.map = mapManager.loadMapFileContent(self.mapName)

        self.mapDrawer = MapDrawer(self.canvasMap, self.map)
        self.mapDrawer.drawMap()
        self.mapDrawer.drawGrid()

    def followingFrame(self):

        # Si aucune map n'a été sélectionnée, on ne continue pas
        if self.map == None:
            return

        # Met à jour la map choisi
        gameManager.setPartyMap(self.map) # a supprimer
        gameManager.setPlacementMethod(self.stringVarRadioButton) # a supprimer
        gamePlayerList = playerManager.PLAYER_LIST
        robotsPosition = None
        if self.stringVarRadioButton == "SPREAD_ROBOTS":
            minSpreadDistance = int(self.scalebarMinSpreadDistance.get())
            robotsPosition = mapUtils.generateRandomSpreadRobotPositions(self.map, len(gamePlayerList), minSpreadDistance)
        else:
            robotsPosition = mapUtils.generateEquidistanceRobotsPositions(self.map, len(gamePlayerList))

        for i in range(len(gamePlayerList)):
            player = gamePlayerList[i]
            position = robotsPosition[i]
            player.getRobotParty().move(position)
            self.map.updateRobotPosition(player.getRobotParty(), position)

        rootManager.runNewFrame(FPParty(self, self.map))
        

    def updateRadioButton(self):
        """
        Affiche la scalebar si mode spreadplayers
        Supprime la scalebar si mode equidistance
        """
        if (self.stringVarRadioButton.get() == "EQUIDISTANCE"):
            if (self.scalebarMinSpreadDistance != None):
                self.scalebarMinSpreadDistance.destroy()
                self.scalebarMinSpreadDistance = None

        elif (self.stringVarRadioButton.get() == "SPREAD_ROBOTS" and self.scalebarMinSpreadDistance == None):
            self.scalebarMinSpreadDistance = super().createScalebar(master=self.frameLeftTop, text="Distance minimale entre chaque robot",
                from_=1, to=5, defaultValue=2, tickInterval=1, resolution=1, length=400)
            self.scalebarMinSpreadDistance.pack()