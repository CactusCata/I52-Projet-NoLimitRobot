from random import randint
from math import sqrt

from robot.robotFile import RobotFile
from map.mine import *
from map.map import Map

robotingame = []

class RobotParty():

    def __init__(self, id, x, y, L_inst, map, energy=500, detec = 4):
        """
        Initialise l'instance du Robot dans la partie.
        Ici sera stocké son énergie, qui descendra lors de la partie, comprise
        entre 500 et 3000 points, ainsi que sa position sur la carte, et enfin la
        distance de détection du robot.
        La position x = 0 et y = 0 est dans la même norme que les canvas de Tkinter,
        i.e en haut à gauche.
        La distance de détection sera initialisée au départ de la partie et surtout
        sera identique pour chaque robot.
        """

        self.__id = id
        self.__energy = energy
        self.__x = x
        self.__y = y
        self.__detec = detec
        self.__L_inst = L_inst
        self.__invisible = False
        robotingame.append(self)
        map.modify(x, y, 2)


    def get_energy(self):
        return self.__energy

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_detec(self):
        return self.__detec

    def print_id(self):
        print(f"Identifiant du robot : {self.__id}")

    def print_energy(self):
        print(f"Energie actuelle du robot : {self.__energy}")

    def print_position(self):
        print(f"Position actuelle du robot : ({self.__x},{self.__y})")

    def print_detec(self):
        print(f"La distance de repérage des robots est de {self.__detec} cases")

    #Instructions des robots#

    def DD(self, direction, map):
        """
        Déplace le robot dans la direction donnée si il n'y a pas de rocher ou de
        robot.
        Celui-ci dépense donc 5 d'énergie, et s'il marche/roule sur une mine,
        il perd 200 d'énergie et rentre dans le mode de secours de par la
        fonction danger()
        """
        self.__energy -= 5

        if (direction == 'H') and (self.__x > 0):
            upslot = map.get(self.__x - 1, self.__y)
            if (upslot == 0):
                self.__x -= 1
            elif (upslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__x -= 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                robot_x = self.__x
                robot_y = self.__y
                map.modify(robot_x, robot_y, 2)
                remove_Mine(robot_x, robot_y)

        elif (direction == "B") and (self.__x < 20):
            downslot = map.get(self.__x + 1, self.__y)
            if (downslot == 0):
                self.__x += 1
            elif (downslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__x += 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                map.modify(self.__x, self.__y, 2)
                remove_Mine(self.__x, self.__y)

        elif (direction == "G") and (self.__y > 0):
            leftslot = map.get(self.__x, self.__y - 1)
            if (leftslot == 0):
                self.__y -= 1
            elif (leftslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__y -= 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                map.modify(self.__x, self.__y, 2)
                remove_Mine(self.__x, self.__y)

        elif (direction == "D") and (self.__y < 30):
            rightslot = map.get(self.__x, self.__y + 1)
            if (rightslot == 0):
                self.__y += 1
            elif (rightslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__y += 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                map.modify(self.__x, self.__y, 2)
                remove_Mine(self.__x, self.__y)

    def AL(self, map):
        """
        Déplace le robot dans une direction aléatoire si il n'y a pas de rocher
        ou de robot.
        Celui-ci dépense donc 5 d'énergie, et s'il marche/roule sur une mine,
        il perd 200 d'énergie et rentre dans le mode de secours de par la
        fonction danger()
        """
        L = ['H', 'B', 'G', 'D']
        rand_num = randint(0,3)
        direction = L[rand_num]
        self.__energy -= 1

        if direction == 'H':
            upslot = map.get(self.__x - 1, self.__y)
            if (upslot == 0):
                self.__x -= 1
            elif (upslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__x -= 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                map.modify(self.__x, self.__y, 2)
                remove_Mine(self.__x, self.__y)

        elif direction == 'B':
            downslot = map.get(self.__x + 1, self.__y)
            if (downslot == 0):
                self.__x += 1
            elif (downslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__x += 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                map.modify(self.__x, self.__y, 2)
                remove_Mine(self.__x, self.__y)

        elif direction == 'G':
            leftslot = map.get(self.__x + 1, self.__y)
            if (leftslot == 0):
                self.__y -= 1
            elif (leftslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__y -= 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                map.modify(self.__x, self.__y, 2)
                remove_Mine(self.__x, self.__y)

        elif direction == 'D':
            rightslot = map.get(self.__x + 1, self.__y)
            if (rightslot == 0):
                self.__y += 1
                map.modify(self.__x, self.__y, 2)
            elif (rightslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__y += 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                map.modify(self.__x, self.__y, 2)
                remove_Mine(self.__x, self.__y)

            #COMPLETER IMPORTANT GERER ID POUR LES MINES

    def MI(self, map):
        """
        Le robot pose une mine autour de lui de manière aléatoire. Si obstacle il y a,
        il est dans l'incapacité de poser à nouveau une mine.
        """
        L = ['H', 'B', 'G', 'D']
        rand_num = randint(0,3)
        direction = L[rand_num]

        self.__energy -= 10

        if direction == 'H':
            xp = self.__x - 1
            yp = self.__y
            upslot = map.get(xp, yp)
            if (upslot == 0):
                robot_id = self.__id
                Mine(xp, yp, robot_id) #Ajout d'une mine non nommée dans la liste des mines
                map.modify(xp, yp, 3) #Modif de la case qui n'est plus vide

        if direction == 'B':
            xp = self.__x + 1
            yp = self.__y
            downslot = map.get(self.__x + 1, self.__y)
            if (downslot == 0):
                robot_id = self.__id
                Mine(xp, yp, robot_id) #Ajout d'une mine non nommée dans la liste des mines
                map.modify(xp, yp, 3) #Modif de la case qui n'est plus vide

        if direction == 'G':
            xp = self.__x
            yp = self.__y - 1
            leftslot = map.get(self.__x, self.__y - 1)
            if (leftslot == 0):
                robot_id = self.__id
                Mine(xp, yp, robot_id) #Ajout d'une mine non nommée dans la liste des mines
                map.modify(xp, yp, 3) #Modif de la case qui n'est plus vide

        if direction == 'D':
            xp = self.__x
            yp = self.__y + 1
            rightslot = map.get(self.__x, self.__y + 1)
            if (rightslot == 0):
                robot_id = self.__id
                Mine(xp, yp, robot_id) #Ajout d'une mine non nommée dans la liste des mines
                map.modify(xp, yp, 3) #Modif de la case qui n'est plus vide

    def IN(self, map):
        """
        Met le robot dans l'état invisible pour le tour de cette instruction.
        """
        self.__invisible = True
        self.__energy -= 20
        #Ne pas oublier de traiter le cas où au prochain tour le robot n'est plus invisible

    def PS(self, map, tested = False):

        if tested == False :
            return 1
        else:
            return 1

    def distance(self, robot2):
        """
        Calcule la distance entre le robot courant et un autre robot sur le terrain.
        """
        return sqrt((self.__x - robot2.__x)**2 + (self.__y - robot2.__y)**2)

    def get_All_Distances(self, robotingame = robotingame):
        """
        Retourne une liste de toutes les distances entre le robot courant et tous
        les robots sur le terrain.
        La liste retournée est une liste de tuple avec en paramètres la longueur et
        l'identifiant du robot non courant.
        """
        for r in robotingame:
            if self.__id() != r.__id():
                return 1


    def danger(self):
        return 1
