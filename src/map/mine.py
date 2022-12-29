class Mine():

    def __init__(self, x, y, damage, playerID):
        self.__x = x
        self.__y = y
        self.__playerID = playerID
        self.__damage = damage


    def get_damage(self):
        return self.__damage

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_playerId(self):
        return self.__playerID

    def print_position(self):
        print(f"Position actuelle de la mine : ({self.__x},{self.__y})")

    def print_id(self):
        print(f"Identifiant de la mine : {self.__id}")

    def copy(self):
        return Mine(self.get_x(), self.get_y(), self.get_damage(), self.get_playerId())