class IInstruction():
    """
    Classe mère des instructions
    """

    def __init__(self, name, cost, damage=-1, resume="", message=""):
        """
        name: nom de l'instruction
        cost: cout en energie du robot
        damage: dégats qu'il faudra appliquer à la cible si l'instruction fait des degats
        resumé: bref résumé de l'instruction
        message: explication complète de l'instruction
        """
        self.name = name
        self.cost = cost
        self.damage = damage
        self.resume = resume
        self.message = message

    def make(self, **kwargs):
        """
        
        """
        print(f"make() function for instruction {self.name} has not been definied")

    def doDamage(self):
        """
        Renvoie True si l'instruction fait des dégats
        """
        return self.damage != -1

    def decreaseRobotEnergy(self, robot):
        """
        Diminue l'energie du robot en fonction du cout de l'instruction
        """
        robot.decreaseEnery(self.cost)

    def getInfo(self):
        """
        Sérialise la classe
        """
        info = ""
        info += f"Instruction: {self.name}\n"
        info += f"Cout: {self.cost}\n"
        if (self.doDamage()):
            info += f"dégats: {self.damage}\n"
        info += f"{self.resume}\n"
        info += f"{self.message}"
        return info