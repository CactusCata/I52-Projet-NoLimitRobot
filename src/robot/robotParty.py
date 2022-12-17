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
        La liste d'instruction sera la liste initialisée par la classe RobotFile.
        L'état invisible vaudra True si invisible, False sinon.
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

    def get_id(self):
        return self.__id

    def get_state(self):
        return self.__invisible

    def print_id(self):
        print(f"Identifiant du robot : {self.__id}")

    def print_energy(self):
        print(f"Energie actuelle du robot : {self.__energy}")

    def print_position(self):
        print(f"Position actuelle du robot : ({self.__x},{self.__y})")

    def print_detec(self):
        print(f"La distance de repérage des robots est de {self.__detec} cases")

#    def check_Energy(self):
#        """
#        Méthode à appelé à chaque instruction afin de voir si il reste de la vie
#        ou non au robot.
#        """
#        if self.__energy > 0:
#            return True
#        else:
#            return False
# Pour le moment, laissé en commentaire car à mettre dans la classe Robot ou plutôt
#                            dans la classe Party ???

    #Instructions des robots#

    def DD(self, direction, map):
        """
        Déplace le robot dans la direction donnée si il n'y a pas de rocher ou de
        robot. Retourne True si déplacement fait, False sinon.
        Celui-ci dépense donc 5 d'énergie, et s'il marche/roule sur une mine,
        il perd 200 d'énergie et rentre dans le mode de secours de par la
        fonction danger()
        """
        self.__energy -= 5

        if (direction == 'H') and (self.__x > 0):
            upslot = map.get(self.__x - 1, self.__y)
            if (upslot == 0):
                self.__x -= 1
                return True
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
                return True

        elif (direction == "B") and (self.__x < 20):
            downslot = map.get(self.__x + 1, self.__y)
            if (downslot == 0):
                self.__x += 1
                return True
            elif (downslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__x += 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                robot_x = self.__x
                robot_y = self.__y
                map.modify(robot_x, robot_y, 2)
                remove_Mine(robot_x, robot_y)
                return True

        elif (direction == "G") and (self.__y > 0):
            leftslot = map.get(self.__x, self.__y - 1)
            if (leftslot == 0):
                self.__y -= 1
                return True
            elif (leftslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__y -= 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                robot_x = self.__x
                robot_y = self.__y
                map.modify(self.__x, self.__y, 2)
                remove_Mine(self.__x, self.__y)
                return True

        elif (direction == "D") and (self.__y < 30):
            rightslot = map.get(self.__x, self.__y + 1)
            if (rightslot == 0):
                self.__y += 1
                return True
            elif (rightslot == 3):
                id_mine = check_Id_Mine(self, direction)
                self.__y += 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                robot_x = self.__x
                robot_y = self.__y
                map.modify(self.__x, self.__y, 2)
                remove_Mine(self.__x, self.__y)
                return True

        return False

    def DDbis(self, direction, map):
        """
        Méthode utilisée uniquement dans PS et FT. Elle effectue un déplacement
        déterministe en diagonale si possible. Retourne True si déplacement fait,
        False sinon.
        """
        if (direction == "HG") and (self.__x > 0) and (self.__y > 0):
            upslot = map.get(self.__x - 1, self.__y - 1)
            if (upslot == 0):
                self.__x -= 1
                self.__y -= 1
                return True
            elif (upslot == 3):
                id_mine = check_Id_Minebis(self, direction)
                self.__x -= 1
                self.__y -= 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                robot_x = self.__x
                robot_y = self.__y
                map.modify(robot_x, robot_y, 2)
                remove_Mine(robot_x, robot_y)
                return True

        elif (direction == "BD") and (self.__x < 20) and (self.__y < 30):
            downslot = map.get(self.__x + 1, self.__y + 1)
            if (downslot == 0):
                self.__x += 1
                self.__y += 1
                return True
            elif (downslot == 3):
                id_mine = check_Id_Minebis(self, direction)
                self.__x += 1
                self.__y += 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                robot_x = self.__x
                robot_y = self.__y
                map.modify(robot_x, robot_y, 2)
                remove_Mine(robot_x, robot_y)
                return True

        elif (direction == "BG") and (self.__x < 20) and (self.__y > 0):
            leftslot = map.get(self.__x, self.__y - 1)
            if (leftslot == 0):
                self.__x += 1
                self.__y -= 1
                return True
            elif (leftslot == 3):
                id_mine = check_Id_Minebis(self, direction)
                self.__x += 1
                self.__y -= 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                    robot_x = self.__x
                    robot_y = self.__y
                map.modify(robot_x, robot_y, 2)
                remove_Mine(robot_x, robot_y)
                return True

        elif (direction == "HD") and (self.__x > 0) and (self.__y < 30):
            rightslot = map.get(self.__x, self.__y + 1)
            if (rightslot == 0):
                self.__x -= 1
                self.__y += 1
                return True
            elif (rightslot == 3):
                id_mine = check_Id_Minebis(self, direction)
                self.__x += 1
                self.__y += 1
                if id_mine != self.__id:
                    self.__energy -= 200
                    self.danger()
                robot_x = self.__x
                robot_y = self.__y
                map.modify(robot_x, robot_y, 2)
                remove_Mine(robot_x, robot_y)
                return True

        return False

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
                id_mine = check_Id_Mine(self.__x, self.__y, direction)
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
                id_mine = check_Id_Mine(self.__x, self.__y, direction)
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
                id_mine = check_Id_Mine(self.__x, self.__y, direction)
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
                id_mine = check_Id_Mine(self.__x, self.__y, direction)
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

    def IN(self):
        """
        Met le robot dans l'état invisible pour le tour de cette instruction.
        """
        self.__invisible = True
        self.__energy -= 20
        #Ne pas oublier de traiter le cas où au prochain tour le robot n'est plus invisible

    def PS(self, map):
        """
        Déplace le robot courant d'une case dans la direction du robot le plus
        proche. Si tested vaut True, alors un test de distance de repérage sera
        fait.
        """
        nearest_robot = self.get_Min_Distance()
        self.__energy -= 4
        print(f"Position robot plus proche : {nearest_robot[0]}")
        self.moving(nearest_robot[1], 0, map)

    def FT(self, map):
        """
        Déplace le robot courant d'une case dans la direction opposée au robot le
        plus proche.Si tested vaut True, alors un test de distance de repérage sera
        fait.
        """
        nearest_robot = self.get_Min_Distance()
        self.__energy -= 4
        print(f"Position robot plus proche : {nearest_robot[0]}")
        self.moving(nearest_robot[1], 1, map)

    def TT(self, map, instr1, instr2):
        """
        Fonction de test de repérage. Si le robot ennemi le plus proche est à une
        distance inférieur ou égale à la distance de repérage des robots, alors
        on exécute la première instruction, sinon la deuxième si supérieur.
        """
        nearest_robot = self.get_Min_Distance()
        if nearest_robot[0] < self.__detec:
            self.execute_Instruction(map, instr1, self)
        else:
            self.execute_Instruction(map, instr2, self)

    def TH(self, map):
        rand_num = randint(0,1)
        if rand_num == 0:
            direction = 'G'
        else:
            direction = 'D'

        self.get_entity_in_range(map, direction)
        self.__energy -= 3

    def TV(self, map):
        rand_num = randint(0,1)
        if rand_num == 0:
            direction = 'H'
        else:
            direction = 'B'

        self.get_entity_in_range(map, direction)
        self.__energy -= 3

    #Methodes Utilitaires#

    def distance(self, robot2):
        """
        Calcule la distance entre le robot courant et un autre robot sur le terrain.
        """
        return sqrt((self.__x - robot2.__x)**2 + (self.__y - robot2.__y)**2)

    def get_All_Distances(self, robotingame = robotingame):
        """
        Retourne une liste de toutes les distances entre le robot courant et tous
        les robots visibles sur le terrain.
        La liste retournée est une liste de tuple avec en paramètres la longueur et
        le robot non courant.
        """
        L = []
        for r in robotingame:
            if (self.__id != r.__id) and (r.__invisible != 1) :
                L.append((self.distance(r), r))

        return L

    def get_Min_Distance(self, robotingame = robotingame):
        """
        Retourne un tuple composé de la distance entre le robot courant et le robot
        le plus proche, ainsi que de l'identifiant du robot le plus proche.
        """
        L_distances = self.get_All_Distances()
        min_dist = L_distances[0]
        for i in range (1,len(L_distances)):
            if L_distances[i][0] < min_dist[0]:
                min_dist = L[i][0]

        return min_dist

    def moving(self, robot2, action, map):
        """
        Déplace le robot de manière à ce que celui-ci pourchasse l'adversaire si
        action == 0, sinon si action == 1, le robot courant fuit l'adversaire.
        """
        xp = self.__x - robot2.get_x()
        yp = self.__y - robot2.get_y()
        direction1 = ""
        direction2 = ""
        diagonal = ""

        if xp < 0: #Si négatif alors adversaire vers le bas
            if action == 0: #Si pourchasse
                direction1 += 'B'
            else: #Sinon fuite
                direction1 += 'H'

        elif xp > 0: #Si positif alors adversaire vers le haut
            if action == 0:
                direction1 += 'H'
            else:
                direction1 += 'B'

        if yp < 0: #Si négatif alors adversaire vers la droite
            if action == 0:
                direction2 += 'D'
            else:
                direction2 += 'G'

        elif yp > 0: #Si positif alors adversaire vers la gauche
            if action == 0:
                direction2 += 'G'
            else:
                direction2 += 'D'

        diagonal += direction1 + direction2

        if not (self.DDbis(diagonal, map)):
            if not (self.DD(direction1, map)):
                self.DD(direction2, map)

    def execute_Instruction(self, map, instr, robot):
        if instr == "AL":
            robot.AL(map)
        elif instr == "MI":
            robot.MI(map)
        elif instr == "IN":
            robot.IN()
        elif instr == "PS":
            robot.PS(map)
        elif instr == "FT":
            robot.FT(map)
        elif instr == "TH":
            robot.TH()
        elif instr == "TV":
            robot.TV()

    def get_entity_in_range(self, map, direction):
        i = 1
        x_bullet = self.__x
        y_bullet = self.__y
        if direction == 'H':
            while (x_bullet > 0) and (i < self.__detec):
                entity_type = map.get(x_bullet-1, y_bullet)
                if entity_type == 1:
                    return True
                elif entity_type == 2:
                    entity_robot = check_Robot(x_bullet, y_bullet, direction)
                    if entity_robot != None:
                        entity_robot.__energy -= 20
                elif entity_type == 3:
                    id_mine = check_Id_Mine(x_bullet, y_bullet, direction)
                    if id_mine != self.__id:
                        remove_Mine(x_bullet, y_bullet)
                        return True
                else:
                    x_bullet -= 1
                i += 1

        if direction == 'B':
            while (x_bullet < 20) and (i < self.__detec):
                entity_type = map.get(x_bullet+1, y_bullet)
                if entity_type == 1:
                    return True
                elif entity_type == 2:
                    entity_robot = check_Robot(x_bullet, y_bullet, direction)
                    if entity_robot != None:
                        entity_robot.__energy -= 20
                        return True
                elif entity_type == 3:
                    id_mine = check_Id_Mine(x_bullet, y_bullet, direction)
                    if id_mine != self.__id:
                        remove_Mine(x_bullet, y_bullet)
                        return True
                else:
                    x_bullet += 1
                i += 1

        if direction == 'G':
            while (y_bullet > 0) and (i < self.__detec):
                entity_type = map.get(x_bullet, y_bullet-1)
                if entity_type == 1:
                    return True
                elif entity_type == 2:
                    entity_robot = check_Robot(x_bullet, y_bullet, direction)
                    if entity_robot != None:
                        entity_robot.__energy -= 20
                    return True
                elif entity_type == 3:
                    id_mine = check_Id_Mine(x_bullet, y_bullet, direction)
                    if id_mine != self.__id:
                        remove_Mine(x_bullet, y_bullet)
                        return True
                else:
                    y_bullet -= 1
                i += 1

        if direction == 'D':
            while (y_bullet < 30) and (i < self.__detec):
                entity_type = map.get(x_bullet, y_bullet+1)
                if entity_type == 1:
                    return True
                elif entity_type == 2:
                    entity_robot = check_Robot(x_bullet, y_bullet, direction)
                    if entity_robot != None:
                        entity_robot.__energy -= 20
                    return True
                elif entity_type == 3:
                    id_mine = check_Id_Mine(x_bullet, y_bullet, direction)
                    if id_mine != self.__id:
                        remove_Mine(x_bullet, y_bullet)
                        return True
                else:
                    y_bullet += 1
                i += 1

        return False

    def danger(self):
        return 1 #Compléter MAIS ptet pas au bon endroit, à voir pour la classe
                #Party

def check_Robot(x, y, direction, robotingame = robotingame):
    """
    Renvoie le robot situé dans la direction du projectile.
    """
    i = 0
    if direction == 'H':
        xp = x - 1
        yp = y
    elif direction == 'B':
        xp = x + 1
        yp = y
    elif direction == 'G':
        xp = x
        yp = y - 1
    else:
        xp = x
        yp = y + 1
    while (robotingame[i].get_x() != xp) and (robotingame[i].get_y() != yp):
        i += 1

    if robotingame[i].get_state() != True:
        return robotingame[i]
