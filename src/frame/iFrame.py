import frame.rootManager as rootManager

import utils.fileUtils as filsUtils

from tkinter import Button, Label, Text, Scale, Frame, Canvas
from tkinter.ttk import Combobox, Checkbutton
from PIL import Image, ImageTk

class IFrame():

    def __init__(self, previousFrame=None):
        self.items = []
        self.previousFrame = previousFrame

    def createFrame(self, master=None):
        """
        Crée une frame

            - master: Si n'est pas utilisé, alors prend la valeur de rootManager.getRoot
        """
        if (master is None):
            master = rootManager.getRoot()

        frame = Frame(master, bg='#1E1E1E')
        self.registerItem(frame)
        return frame

    def createCanvas(self, master=None, width=10, height=10):
        """
        Crée un canvas

            - master: Si n'est pas utilisé, alors prend la valeur de rootManager.getRoot
            - (width, height): dimensions du canvas
        """
        if (master is None):
            master = rootManager.getRoot()

        canvas = Canvas(master, bg='#1E1E1E')
        self.registerItem(canvas)
        return canvas

    def drawImage(self, master=None, path="", posX=0, posY=0):
        """
        Crée une image

            - master: Si n'est pas utilisé, alors prend la valeur de rootManager.getRoot
            - text: Chemin du fichier
            - (posX, posY): place l'image aux coordonnées demandées
        """
        if (not filsUtils.fileExist(path)):
            print(f"Le fichier \"{path}\"n'existe pas")
            return

        if (master is None):
            master = rootManager.getRoot()

        img = Image.open(path)
        tatras = ImageTk.PhotoImage(img)
        canvas = self.createCanvas(width=img.size[0] + posX, height=img.size[1] + posY)
        imgId = canvas.create_image(posX, posY, image=tatras)
        self.registerItem(imgId)


    def createButton(self, master=None, text="", cmd=None, fontSize=14):
        """
        Crée un bouton

            - master: Si n'est pas utilisé, alors prend la valeur de rootManager.getRoot
            - text: Texte du bouton
            - cmd: fonction executée lorsque l'utilisateur appuie sur le bouton
            - fontSize: taille de la police d'écriture du texte
        """
        if (master is None):
            master = rootManager.getRoot()

        button = Button(master, text=text, command=cmd, bg="#1E1E1E", fg="#ABB2B9", font=("Arial", fontSize))
        self.registerItem(button)
        return button

    def createLabel(self, master=None, text="", fontSize=14):
        """
        Crée un label

            - master: Si n'est pas utilisé, alors prend la valeur de rootManager.getRoot
            - text: Texte du label
            - fontSize: taille de la police d'écriture du texte
        """
        if (master is None):
            master = rootManager.getRoot()

        label = Label(master, text=text, bg="#1E1E1E", fg="#ABB2B9", font=("Arial", fontSize))
        self.registerItem(label)
        return label

    def createTextBox(self, master=None, defaultText="", width=10, height=1, fontSize=14):
        """
        Crée une boite à texte

            - master: Si n'est pas utilisé, alors prend la valeur de rootManager.getRoot
            - defaultText: Texte par défaut au moment de l'initialisation de la boite à texte
            - width: Nombre de pixel en largeur de la boite à texte
            - height: Nombre de pixel en hauteur de la boite à texte
            - fontSize: taille de la police d'écriture du texte
        """
        if (master is None):
            master = rootManager.getRoot()

        textBox = Text(master, width=width, height=height, bg='#1E1E1E', fg='#ABB2B9', font=("Arial", fontSize))
        textBox.insert(1.0, defaultText)
        self.registerItem(textBox)
        return textBox

    def createCheckButton(self, master=None, text="", callback=None):
        if (master is None):
            master = rootManager.getRoot()

        checkButton = Checkbutton(master, text=text, command=callback)
        self.registerItem(checkButton)
        return checkButton


    def createScalebar(self, master=None, text="", orientation="horizontal", from_=0, to=10, defaultValue=None, length=100, tickInterval=2, resolution=1, fontSize=14):
        """
        Crée une échelle

            - master: Si n'est pas utilisé, alors prend la valeur de rootManager.getRoot
            - text: Texte situé à proximité de l'échelle
            - orientation: "horizontal" ou "vertical"
            - from_: Valeur minimal de l'échelle
            - to: Valeur maximal de l'échelle
            - defaultValue: Valeur initiale du curseur de l'échelle
            - length: Longueur de l'échelle en pixel
            - tickInterval: Pas de la graduation de l'échelle
            - resolution: Ecart entre deux valeurs consécutives 
            - fontSize: taille de la police d'écriture du texte
        """
        if (master is None):
            master = rootManager.getRoot()
        
        if defaultValue == None:
            defaultValue = from_

        scalebar = Scale(master, orient=orientation, from_=from_, to=to, resolution=resolution, tickinterval=tickInterval, length=length, label=text, bg='#1E1E1E', fg='#ABB2B9', font=("Arial", fontSize))
        scalebar.set(defaultValue)
        self.registerItem(scalebar)
        return scalebar

    def createComboBox(self, master=None, list=["default"], callback=None, fontSize=14):
        """
        Crée une liste à choix

            - master: Si n'est pas utilisé, alors prend la valeur de rootManager.getRoot
            - list: L'ensemble des chaines de caractères
            - callback: Fonction à executer lorsque la sélection de la liste à choix change
            - fontSize: taille de la police d'écriture du texte
        """
        if (master is None):
            master = rootManager.getRoot()

        combobox = Combobox(self.master, values=list)
        combobox.configure(font=("Arial", fontSize))

        if (callback != None):
            combobox.bind("<<ComboboxSelected>>", callback)

        self.registerItem(combobox)

        return combobox

    def clearFrame(self):
        """
        Supprime tous les objets (widgets, etc...) crées
        """
        print(f"Taille de la liste: {len(self.items)}")
        for item in self.items:
            print("Item has been cleared")
            item.destroy()
        self.items = []

    def registerItem(self, item):
        """
        Renseigne qu'un objet (widget, etc...) a été crée
        """
        self.items.append(item)

    def reopenLastFrame(self):
        if (self.previousFrame is not None):
            rootManager.runNewFrame(self.previousFrame)