import instruction.instructLexicalAnalyser as instructLexicalAnalyser
import instruction.instructSyntaxAnalyser as instructSyntaxAnalyser

from instruction.instructionSyntaxException import InstructionSyntaxException

def instructionsAreValide(textInstruct):
    """
    Renvoie une couple (ligne, col) de l'emplacement
    de l'erreur s'il y en a une, sinon renvoie (-1, -1)
    """

    try:
        lexicalsUnits = instructLexicalAnalyser.analex(textInstruct)
        instructSyntaxAnalyser.axiome(lexicalsUnits)
    except InstructionSyntaxException as error:
        return error.getErrorEmplacement()
    finally:
        return (-1, -1)