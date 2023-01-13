import utils.tkinter.tkUtils as tkUtils

class Param:
    """
    Permet de connaitre à tout instant les paramètres du jeu.
    """

    def __init__(self, fullScreenState=True, needHelpState=True):
        self.fullScreenState = fullScreenState
        self.needHelpState = needHelpState

        # Est-ce que les options ont été modifiées depuis leur chargement
        self.optionsChanged = False

    def optionsHasChanged(self):
        """
        Renvoie True si les options ont été modifiées depuis leur chargement
        Sinon renvoie False
        """
        return self.optionsChanged

    def toggleFullScreen(self, root):
        self.fullScreenState = False if self.fullScreenState else True
        self.applyFullScreenState(root)

    def getFullScreenState(self):
        return self.fullScreenState

    def applyFullScreenState(self, root):
        if self.fullScreenState:
            self.enableFullScreen(root)
        else:
            self.disableFullScreen(root)

    def enableFullScreen(self, root):
        # Dimensionne la fenêtre en fonction de l'écran de l'utilisateur
        # et bloque le dimensionnement de la fenêtre
        dimensions = tkUtils.setupRootGeometry(root, ratio=1.0)
        tkUtils.lockRootDimensions(root, dimensions)

        root.attributes('-fullscreen', True)
        self.fullScreenState = True

        if (not self.optionsChanged):
            self.optionsChanged = True

    def disableFullScreen(self, root):
        dimensions = tkUtils.setupRootGeometry(root, ratio=0.8)
        tkUtils.lockRootDimensions(root, dimensions)
        root.attributes('-fullscreen', False)
        self.fullScreenState = False

        if (not self.optionsChanged):
            self.optionsChanged = True

    def toggleHelp(self):
        self.needHelpState = False if self.needHelpState else True

        if (not self.optionsChanged):
            self.optionsChanged = True

    def isNeedHelp(self):
        return self.needHelpState

    def enableHelp(self):
        self.needHelpState = True

        if (not self.optionsChanged):
            self.optionsChanged = True

    def disableHelp(self):
        self.needHelpState = False

        if (not self.optionsChanged):
            self.optionsChanged = True

    def serializeParam(self):
        return {
            "fullScreenState": self.fullScreenState,
            "needHelpState": self.needHelpState
        }