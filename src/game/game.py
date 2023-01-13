import utils.instructionUtils as instructionUtils
import player.playerManager as playerManager

class Game():
    """
    Permet le déroulement logique d'une partie.
    """

    def __init__(self, map):

        # Carte sur laquelle va se dérouler la partie
        self.map = map

        # Liste des joueurs en vie
        self.alivePlayersIndex = [i for i in range(len(playerManager.PLAYER_LIST))]

        # Prochain joueur qui doit jouer
        self.playerTurnIndex = 0

        # Joueur qui a gagné
        self.winner = None


    def next(self):
        """
        Execute l'instruction du prochain robot
        """

        if (self.isEnded()):
            return

        # Get the good robot turn

        playerTurnIndex = self.alivePlayersIndex[self.playerTurnIndex]
        playerTurn = playerManager.PLAYER_LIST[playerTurnIndex]
        robot = playerTurn.getRobotParty()

        # Execute robot's instruction 
        instructionName = playerTurn.getNextInstructionName()
        instruction = instructionUtils.INSTRUCTION_LIST[instructionName.split(" ")[0]]
        instruction.make(player=playerTurn, map=self.map, cmd=instructionName)

        # If the robot has no left energy, remove it from alive players
        if (robot.get_energy() <= 0):
            self.alivePlayersIndex.remove(playerTurnIndex)
            
            # In case of semi-equality
            if (len(self.alivePlayersIndex) == 1):
                self.winner = playerManager.PLAYER_LIST[self.alivePlayersIndex[0]]
                return

        # Get all deads players on this turn
        deadPlayersIndex = []
        for playerIndex in self.alivePlayersIndex:
            player = playerManager.PLAYER_LIST[playerIndex]
            if player.getRobotParty().get_energy() <= 0:
                deadPlayersIndex.append(playerIndex)

        # Delete all players who's dead on this turn
        for playerIndex in deadPlayersIndex:
            self.alivePlayersIndex.remove(playerIndex)

        # Déclarer une gagnant s'il ne reste qu'un seul joueur
        if (len(self.alivePlayersIndex) == 1):
                self.winner = playerManager.PLAYER_LIST[self.alivePlayersIndex[0]]
                return

        # Let the next player play
        self.playerTurnIndex = (self.playerTurnIndex + 1) % len(self.alivePlayersIndex)

    def getWinner(self):
        """
        Renvoie None tant qu'aucun joueur n'a gagné
        Renvoie une instance de joueur si un joueur a gagné
        """
        return self.winner

    def isEnded(self):
        """
        Renvoie True s'il ne reste qu'un seul joueur
        """
        return len(self.alivePlayersIndex) <= 1

    