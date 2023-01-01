
class RobotParty():

    def __init__(self, x, y):
        """
        Initialise l'instance du Robot dans la partie.
        Ici sera stocké son énergie, qui descendra lors de la partie, comprise
        entre 500 et 3000 points, ainsi que sa position sur la carte, et enfin la
        distance de détection du robot.
        La position x = 0 et y = 0 est dans la même norme quet les canvas de Tkinter,
        i.e en haut à gauche.
        La distance de détection sera initialisée au départ de la partie et surtout
        sera identique pour chaque robot.
        La liste d'instruction sera la liste initialisée par la classe RobotFile.
        L'état invisible vaudra True si invisible, False sinon.

        Données:
            - x: un entier
            - y: un entier
            - energy: entier
            - detect: entier
        """
        self.__energy = 500
        self.__max_energy = 500
        self.__x = x
        self.__y = y
        self.__detec = 4
        self.__vanished = False
        self.__instructionCursor = 0
        self.__onDangerInstruction = False

    def dangerInstructionIsEnabled(self):
        return self.__onDangerInstruction

    def update_instruction_cursor(self, n):
        self.__instructionCursor = n

    def get_instruction_number(self):
        return self.__instructionCursor

    def get_id(self):
        return self.__id

    def set_detection_distance(self, distance_detection):
        self.__detec = distance_detection

    def get_distance_detect(self):
        return self.__detec

    def set_max_energy(self, maxEnergy):
        self.__max_energy = maxEnergy

    def get_energy(self):
        return self.__energy

    def get_max_energy(self):
        return self.__max_energy

    def reset_energy(self):
        self.__energy = self.__max_energy

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def move(self, position):
        self.__x = position[0]
        self.__y = position[1]
        if self.is_vanish():
            self.unvanish()

    def decreaseEnery(self, n):
        if self.__energy - n < 0:
            self.__energy = 0
        else:
            self.__energy -= n

    def copy(self):
        return RobotParty(self.get_x(), self.get_y, self.get_energy(), self.get_detect_distance(), self.is_vanish())

    def is_vanish(self):
        return self.__vanished

    def vanish(self):
        self.__vanished = True

    def unvanish(self):
        self.__vanished = False

    def print_id(self):
        print(f"Identifiant du robot : {self.__id}")

    def print_energy(self):
        print(f"Energie actuelle du robot : {self.__energy}")

    def print_position(self):
        print(f"Position actuelle du robot {self.__id} : ({self.__x},{self.__y})")

    def print_detec(self):
        print(f"La distance de repérage des robots est de {self.__detec} cases")