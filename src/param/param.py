import utils.tkinter.tkUtils as tkUtils

class Param:

    def __init__(self, fullScreenState=True, needHelpState=True):
        self.fullScreenState = fullScreenState
        self.needHelpState = needHelpState
        self.optionsChanged = False

    def optionsHasChanged(self):
        return self.optionsChanged

    def toggleFullScreen(self, root):
        print(f"fullscreen from: {self.fullScreenState}")
        self.fullScreenState = False if self.fullScreenState else True
        print(f"To: {self.fullScreenState}")
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