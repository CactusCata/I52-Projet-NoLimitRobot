import instruction.instructLexicalAnalyser as instructLexicalAnalyser
import instruction.instructSyntaxAnalyser as instructSyntaxAnalyser

from instruction.instructionSyntaxException import InstructionSyntaxException

INSTRUCTION_CORRECT = "correct"

def instructionsAreValide(textInstruct):
    """
    Renvoie "correct" si valide
    sinon renvoie le message d'erreur
    """

    try:
        lexicalsUnits = instructLexicalAnalyser.analex(textInstruct + '\n')
        instructSyntaxAnalyser.axiome(lexicalsUnits)
    except InstructionSyntaxException as error:
        return str(error)
        
    return INSTRUCTION_CORRECT