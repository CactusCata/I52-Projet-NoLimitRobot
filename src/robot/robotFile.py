import utils.robotUtils

class RobotFile():

    def __init__(self, name):
        self.__name = name
        self.__desc = robotFile.get_desc_from_name(name)
        self.instr = robotFile.get_instr_from_name(name)

    def get_name(self):

        return self.__name

    def get_name(self):

        return self.__desc

    def get_instr(self):

        return self.__instr

    def print_name(self):

        print(f"Nom du Robot : {self.__name}")

    def print_desc(self):

        print(f"Description du robot : {self.__desc}")

    def print_instr(self):

        print(f"Les instructions sont les suivantes : ")
        for s in self.__instr:
            print(s)
