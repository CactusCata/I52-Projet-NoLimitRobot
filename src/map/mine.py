from map.map import Map

mineingame = []

class Mine(Map):

    def __init__(self, x, y, id, mineingame = mineingame):
        self.__x = x
        self.__y = y
        self.__id = id
        mineingame.append(self)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_id(self):
        return self.__id

    def print_position(self):
        print(f"Position actuelle de la mine : ({self.__x},{self.__y})")

    def print_id(self):
        print(f"Identifiant de la mine : {self.__id}")

def check_Id_Mine(x, y, direction, mineingame = mineingame):
    """
    Renvoie l'identifiant de la mine située dans la direction auquel va le robot
    ou le projectile.
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
    while (mineingame[i].get_x() != xp) and (mineingame[i].get_y() != yp):
        i += 1

    return mineingame[i].get_id()

def check_Id_Minebis(robot, direction, mineingame = mineingame):
    """
    Renvoie l'identifiant de la mine située dans la direction auquel va le robot
    ou le projectile. Ici la direction ne peut-être qu'une direction diagonale.
    """
    i = 0
    if direction == "HG":
        xp = robot.get_x() - 1
        yp = robot.get_y() - 1
    elif direction == "BD":
        xp = robot.get_x() + 1
        yp = robot.get_y() + 1
    elif direction == "BG":
        xp = robot.get_x() + 1
        yp = robot.get_y() - 1
    else:
        xp = robot.get_x() - 1
        yp = robot.get_y() + 1
    while (mineingame[i].get_x() != xp) and (mineingame[i].get_y() != yp):
        i += 1

    return mineingame[i].get_id()

def remove_Mine(x, y, mineingame = mineingame):
    """
    Retire la mine en position (x,y) car elle a été détruite
    """
    i = 0
    while (mineingame[i].get_x() != x) and (mineingame[i].get_y() != y):
        i += 1
    mineingame = mineingame[:i] + mineingame[i+1:]
