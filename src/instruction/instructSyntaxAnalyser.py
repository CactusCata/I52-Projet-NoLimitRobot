from instruction.instructionSyntaxException import InstructionSyntaxException

lexicalUnits = []
cc = 0
col = 0
line = 0

arrayOfInstructions = []

def getLexicalUnit():
    return lexicalUnits[cc]

def increaseCC():
    """
    Curseur de lecture de la liste lexicalUnits
    """
    global cc

    # Augmente le curseur de la colonne
    increaseCol()

    cc += 1

def increaseLine():
    """
    Augmente la ligne pour le gestionnaire d'exceptions
    """
    global line, col
    line += 1
    col = 0

def increaseCol():
    """
    Augmente la colonne pour le gestionnaire d'exceptions
    """
    global col
    col += len(getLexicalUnit()[1])

def instructs():
    if (cc < len(lexicalUnits)):
        instruct()
        instructs()

def instruct():
    lexicalUnit = getLexicalUnit()
    if (lexicalUnit[0] == "INSTRUCTION"):
        arrayOfInstructions.append(action_simple())
        end_line()
    elif (lexicalUnit[0] == "INSTRUCTION_DIRECTION"):
        increaseCC()
        space()
        dir = direction()
        end_line()
        arrayOfInstructions.append(f"{lexicalUnit[0]} {dir}")
    elif (lexicalUnit[0] == "INSTRUCTION_TEST"):
        increaseCC()
        space()
        action2 = action_simple()
        space()
        action3 = action_simple()
        end_line()
        arrayOfInstructions.append(f"{lexicalUnit[0]} {action2} {action3}")
    else:
        raise InstructionSyntaxException(line, col, "An instruction was waited")

def direction():
    lexicalUnit = getLexicalUnit()
    if (lexicalUnit[0] != "DIRECTION"):
        raise InstructionSyntaxException(line, col, "A direction was waited")
    increaseCC()
    return lexicalUnit[1]

def space():
    lexicalUnit = getLexicalUnit()
    if (lexicalUnit[0] != "SPACE"):
        raise InstructionSyntaxException(line, col, "A space was waited")
    increaseCC()

def end_line():
    global line

    lexicalUnit = getLexicalUnit()
    if (lexicalUnit[0] != "END_LINE"):
        raise InstructionSyntaxException(line, col, "An endline was waited")
    increaseCC()
    increaseLine()
    
    

def action_simple():
    lexicalUnit = getLexicalUnit()
    if (lexicalUnit[0] != "INSTRUCTION"):
        raise InstructionSyntaxException(line, col, "A simple instruction was waited")
    increaseCC()
    return lexicalUnit[1]

def axiome(arrayOfLexicalUnits):
    global lexicalUnits, cc, col, line, arrayOfInstructions

    cc = 0
    col = 0
    line = 0
    arrayOfInstructions = []

    lexicalUnits = arrayOfLexicalUnits
    instructs()

    if (cc != len(lexicalUnits)):
        raise InstructionSyntaxException(line, col, "Error syntax")