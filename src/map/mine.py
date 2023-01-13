class Mine():
    """
    Classe pour les mines
    """

    def __init__(self, x, y, damage, playerID):
        """
            - x: position sur la map
            - y: position sur la map
            - damage: dégats lorsque l'utilisateur marche sur la mine
            - playerID: numero du joueur
        """
        self.__x = x
        self.__y = y
        self.__playerID = playerID
        self.__damage = damage


    def get_damage(self):
        """
        Renvoie les dégats de la mine
        """
        return self.__damage

    def get_x(self):
        """
        Renvoie la position de la mine sur la map
        """
        return self.__x

    def get_y(self):
        """
        Renvoie la position de la mine sur la carte
        """
        return self.__y

    def get_playerId(self):
        """
        Renvoie le numero du joueur sur la carte
        """
        return self.__playerID

    def print_position(self):
        print(f"Position actuelle de la mine : ({self.__x},{self.__y})")

    def print_id(self):
        print(f"Identifiant de la mine : {self.__id}")

    def copy(self):
        return Mine(self.get_x(), self.get_y(), self.get_damage(), self.get_playerId())