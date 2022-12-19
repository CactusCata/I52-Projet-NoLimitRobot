import utils.robotUtils as robotUtils
import image.imageManager as imageManager

class RobotFile():
    """
    Cette classe contient les informations d'un robot
    stockés sous forme de fichier dans config/robots/{nom_robot}/instructions.rbt
    Elle permet également de récuperer le chemin du logo du robot
    ainsi que la possibilité de la charger pour tkinter.
    """

    def __init__(self, name):
        self.__name = name
        self.__desc = robotUtils.get_desc_from_name(name)
        self.__instr = robotUtils.get_instr_from_name(name)
        self.__logoPath = robotUtils.get_logo_path_from_name(name)
        self.__logoImg = None
        self.__logoTk = None

    def get_name(self):
        """
        Renvoie le nom du robot        
        """
        return self.__name

    def get_desc(self):
        """
        Renvoie la description du robot
        """
        return self.__desc

    def get_instr(self):
        """
        Renvoie la liste des instructions du robot
        """
        return self.__instr

    def get_logo_path(self):
        """
        Renvoie le chemin du logo
        """
        return self.__logoPath

    def logo_is_loaded(self):
        """
        Renvoie:
            - True si le logo a bien été chargé
            - False si le logo n'a pas été chargé

        Pour charger le logo du robot, il est nécéssaire
        d'executer la méthode robotFile.load_logo()
        """
        return self.__logoImg != None

    def logo_tk_is_loaded(self):
        """
        Renvoie:
            - True si le logo a bien été chargé
            - False si le logo n'a pas été chargé

        Pour charger le logo du robot, il est nécéssaire
        d'executer la méthode robotFile.load_logo()
        """
        return self.__logoTk != None

    def load_logo(self, dimX=100, dimY=100):
        """
        Charge en mémoire l'image logo du reobot
        """
        if (not self.logo_is_loaded()):
            self.__logoImg = imageManager.loadImage(self.get_logo_path(), dimX=dimX, dimY=dimY)

    def load_logo_tk(self):
        if (not self.logo_tk_is_loaded()):
            self.__logoTk = imageManager.loadImageTk(self.__logoImg)

    def get_logo(self):
        """
        Renvoie une instance de l'image du logo pour tkinter.
        Doit d'abord est chargé via la méthode robotFile.load_logo()
        """
        return self.__logoImg
    
    def get_logo_tk(self):
        return self.__logoTk