import instruction.instructLexicalAnalyser as instructLexicalAnalyser
import instruction.instructSyntaxAnalyser as instructSyntaxAnalyser

from instruction.instructionSyntaxException import InstructionSyntaxException

INSTRUCTION_CORRECT = "correct"

def instructionsAreValide(textInstruct):
    """
    Renvoie un message.
    Si valide renvoie "correct"
    sinon renvoie le message d'erreur
    """

    print(textInstruct)

    try:
        lexicalsUnits = instructLexicalAnalyser.analex(textInstruct + '\n')
        print(lexicalsUnits)
        instructSyntaxAnalyser.axiome(lexicalsUnits)
    except InstructionSyntaxException as error:
        return str(error)
        
    return INSTRUCTION_CORRECT