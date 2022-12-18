from tkinter import messagebox

class TkPerformer:

    def __init__(self, root, title, text):
        self.root = root
        self.title = title
        self.text = text
        
    def run(self):
        """
        Renvoie:
            - 0 si oui
            - 1 si non
            - 2 si annuler
        """
        msg = messagebox.askyesnocancel(
            self.title,
            self.text,
            default=messagebox.YES,
            parent=self.root
        )

        self.root.focus_set()

        if msg:
            return 0
        elif msg is None:
            return 1
        else:
            return 2
