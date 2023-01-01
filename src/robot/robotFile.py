import utils.robotUtils as robotUtils
import image.imageManager as imageManager
import player.playerManager as playerManager

class RobotFile():
    """
    Cette classe contient les informations d'un robot
    stockées sous forme de fichier dans config/robots/{nom_robot}/instructions.rbt
    Elle permet également de récuperer le chemin du logo du robot
    ainsi que la possibilité de la charger pour tkinter.
    """

    def __init__(self, name):
        self.__name = name
        self.__desc = robotUtils.get_desc_from_name(name)
        instructions = robotUtils.get_instr_from_name(name)
        self.__dangerInstruction = instructions[0]
        self.__instr = instructions[1:]
        self.__logoPath = robotUtils.get_logo_path_from_name(name)
        self.__icon = None
        self.__iconTk = None
        self.__bloc = None
        self.__blocTk = None


    def get_danger_instruction(self):
        return self.__dangerInstruction

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

    def enable_danger_instruction(self, index):
        self.__instr[index] = self.__dangerInstruction

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


    def load_icon(self):
        """
        Charge en mémoire l'image logo du reobot
        """
        self.__icon = imageManager.loadImage(self.get_logo_path(), playerManager.PLAYER_ICON_DIMENSIONS)


    def icon_is_loaded(self):
        """
        Renvoie:
            - True si l'icon a bien été chargée
            - False si l'icon n'a pas été chargée

        Pour charger l'icon du robot, il est nécéssaire
        d'executer la méthode robotFile.load_icon()
        """
        return self.__icon != None

    def load_icon_tk(self):
        if (not self.icon_tk_is_loaded()):
            self.__iconTk = imageManager.loadImageTk(self.__icon)

    def icon_tk_is_loaded(self):
        """
        Renvoie:
            - True si l'icon a bien été chargée
            - False si l'icon n'a pas été chargée

        Pour charger l'icon du robot, il est nécéssaire
        d'executer la méthode robotFile.load_icon_tk()
        """
        return self.__iconTk != None


    def get_icon(self):
        """
        Renvoie une instance de l'image du logo pour tkinter.
        Doit d'abord est chargé via la méthode robotFile.load_logo()
        """
        return self.__icon
    
    def get_icon_tk(self):
        return self.__iconTk

    def load_bloc(self):
        """
        Charge en mémoire l'image logo du reobot
        """
        self.__bloc = imageManager.loadImage(self.get_logo_path(), imageManager.MAP_BLOC_DIMENSIONS)


    def bloc_is_loaded(self):
        """
        Renvoie:
            - True si l'bloc a bien été chargée
            - False si l'bloc n'a pas été chargée

        Pour charger l'bloc du robot, il est nécéssaire
        d'executer la méthode robotFile.load_bloc()
        """
        return self.__bloc != None

    def load_bloc_tk(self):
        if (not self.bloc_tk_is_loaded()):
            self.__blocTk = imageManager.loadImageTk(self.__bloc)

    def bloc_tk_is_loaded(self):
        """
        Renvoie:
            - True si l'bloc a bien été chargée
            - False si l'bloc n'a pas été chargée

        Pour charger l'bloc du robot, il est nécéssaire
        d'executer la méthode robotFile.load_bloc_tk()
        """
        return self.__blocTk != None


    def get_bloc(self):
        """
        Renvoie une instance de l'image du logo pour tkinter.
        Doit d'abord est chargé via la méthode robotFile.load_logo()
        """
        return self.__bloc
    
    def get_bloc_tk(self):
        return self.__blocTk