class IInstruction():

    def __init__(self, name, cost, damage=-1, resume="", message=""):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.resume = resume
        self.message = message

    def make(self, **kwargs):
        print(f"make() function for instruction {self.name} has not been definied")

    def doDamage(self):
        return self.damage != -1

    def decreaseRobotEnergy(self, robot):
        robot.decreaseEnery(self.cost)

    def getInfo(self):
        info = ""
        info += f"Instruction: {self.name}\n"
        info += f"Cout: {self.cost}\n"
        if (self.doDamage()):
            info += f"dégats: {self.damage}\n"
        info += f"{self.resume}\n"
        info += f"{self.message}"
        return info