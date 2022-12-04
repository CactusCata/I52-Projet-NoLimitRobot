import frame.rootManager as rootManager

from frame.iFrame import IFrame

class FTest(IFrame):

    def draw(self):
        root = rootManager.getRoot()

        b1 = super().createButton(text="autre", cmd=self.autreButton)
        b1.pack()

    def autreButton(self):
        print("dawn les gens c'est tibo")
        pass
