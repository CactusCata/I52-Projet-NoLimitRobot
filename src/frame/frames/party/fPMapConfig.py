import frame.rootManager as rootManager
import map.mapManager as mapManager
import player.playerManager as playerManager

from frame.messagesHelp import HELP_FPMAPCONFIG
from map.mapDrawer import MapDrawer
import utils.mapUtils as mapUtils

from frame.iFrame import IFrame
from frame.frames.party.fPParty import FPParty

from tkinter import StringVar

class FPMapConfig(IFrame):
    """
    Propose à l'utilisateur de choisir une carte/arène où les robots
    s'affronteront. Permet aussi de choisir un mode de placement des
    robots (equidistance ou aléatoire).
    """

    def __init__(self, previousFrame):
        super().__init__(previousFrame, HELP_FPMAPCONFIG)

        # Scalebar de la distance minimum si mode de répartition aléatoire
        self.scalebarMinSpreadDistance = None
        self.labelScalebar = None

        # Carte choisie
        self.map = None

        # Positions des robots après le choix de la répartition
        self.robotsPosition = []

        # Déssineur de carte
        self.mapDrawer = None

    def draw(self):

        super().createButtonHelp()

        frameLeft = super().createFrame()
        frameLeft.pack(side="left", ipadx=50)

        self.frameLeftTop = super().createFrame(master=frameLeft)
        self.frameLeftTop.pack(side="top", ipady=20)
        frameLeftBot = super().createFrame(master=frameLeft)
        frameLeftBot.pack(side="bottom", ipady=20)

        frameRight = super().createFrame()
        frameRight.pack(side="right", ipadx=50)

        # Choix de la map
        labelMapName = super().createLabel(master=self.frameLeftTop, text="Choisir la map:")
        labelMapName.pack()
        self.comboBoxMapName = super().createComboBox(master=self.frameLeftTop, list=mapManager.getLoadedMaps(), callback=lambda event: self.mapSelectedChanged(event))
        self.comboBoxMapName.pack()

        # Map dessinée
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

        # Afficher de nouveau la scalebar si l'utilisateur appuie sur le bouton de retour
        #self.updateRadioButton()

        # Confirmer
        buttonConfirm = super().createButton(master=frameLeftBot, text="Voir la partie", cmd=lambda:self.followingFrame())
        buttonConfirm.pack()

        # Retour
        buttonBack = super().createButton(master=frameLeftBot, text="Retour", cmd=lambda:self.tryToGoBack())
        super().modifyButton(buttonBack ,bg = "darkred", ab = "red")
        buttonBack.pack(side="bottom", anchor="w", padx=10, pady=10)

    def tryToGoBack(self):
        """
        Fonction appelée lorsque l'utilisateur souhaite
        revenir en arrière
        """
        self.mapDrawer.stopDrawIPs()
        super(FPMapConfig, self).reopenLastFrame()

    def mapSelectedChanged(self, event):
        """
        Evenement déclanché lorsque l'utilisateur choisi une carte.
        Quand appelé, la carte est déssinée et des points d'intérrogations
        sont déssinés à l'emplacement des robots en fonction de du mode
        de répartition de ceux-ci.
        """

        self.mapName = self.comboBoxMapName.get()

        # object map associé
        self.map = mapManager.loadMapFileContent(self.mapName)

        # Si d'anciens points d'intérrogations sont déssinés,
        # ne plus les déssiner
        if (self.mapDrawer != None):
            self.mapDrawer.stopDrawIPs()

        # (Re-)Initialisation du déssineur de carte
        # et dessin de la carte
        self.mapDrawer = MapDrawer(self.canvasMap, self.map)
        self.mapDrawer.drawMap()
        self.mapDrawer.drawGrid()
        if self.scalebarMinSpreadDistance == None:
            self.robotsPosition = mapUtils.generateEquidistanceRobotsPositions(self.map, len(playerManager.PLAYER_LIST))
            self.mapDrawer.startDrawIPs(self.robotsPosition)
        else:
            self.mapDrawer.startDrawBigIP()

    def followingFrame(self):
        """
        Méthode appelée lorsque l'utilisateur décide de confirmer
        ses choix
        """

        # Si aucune map n'a été sélectionnée, on annule
        if self.map == None or self.mapDrawer == None:
            return

        # Créé la positions des robots
        if self.scalebarMinSpreadDistance != None:
            minSpreadDistance = int(self.scalebarMinSpreadDistance.get())
            self.robotsPosition = mapUtils.generateRandomSpreadRobotPositions(self.map, len(playerManager.PLAYER_LIST), minSpreadDistance)

        # Applique la position des robots à la carte
        for i in range(len(playerManager.PLAYER_LIST)):
            player = playerManager.PLAYER_LIST[i]
            position = self.robotsPosition[i]
            self.map.updateRobotPosition(player.getRobotParty(), position)

        # On arrête de déssiner les points d'intérrogation
        self.mapDrawer.stopDrawIPs()
        self.mapDrawer.clear()

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
                self.labelScalebar.destroy()
                self.labelScalebar = None
            if (self.mapDrawer != None):
                self.mapDrawer.startDrawIPs(self.robotsPosition)

        elif (self.stringVarRadioButton.get() == "SPREAD_ROBOTS" and self.scalebarMinSpreadDistance == None):
            self.labelScalebar = super().createLabel(master=self.frameLeftTop, text="Distance minimale entre chaque robot")
            self.labelScalebar["wraplength"] = int(0.1 * rootManager.getRoot().winfo_width())
            self.labelScalebar.pack()
            self.scalebarMinSpreadDistance = super().createScalebar(master=self.frameLeftTop, orientation="vertical",
                from_=1, to=5, defaultValue=2, tickInterval=1, resolution=1, length=200)
            self.scalebarMinSpreadDistance.pack()
            if (self.mapDrawer != None):
                self.mapDrawer.startDrawBigIP()
