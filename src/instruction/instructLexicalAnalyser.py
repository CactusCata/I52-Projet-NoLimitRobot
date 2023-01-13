from instruction.instructionSyntaxException import InstructionSyntaxException

from utils.instructionUtils import MOUVEMENT_LIST

def isString(s, startIndex, stringWanted):
    for i in range(len(stringWanted)):
        if (s[i + startIndex] != stringWanted[i]):
            return False
    return True

def analex(text):
    """
    Analyse lexicale du texte
    """
    arrayOfLexicalsUnits = []

    i = 0
    line = 0
    col = 0
    while i < len(text):
        if (isString(text, i, "DD")):
            i += 2
            col += 2
            arrayOfLexicalsUnits.append(["INSTRUCTION_DIRECTION", "DD"])

        elif (isString(text, i, "AL")):
            i += 2
            col += 2
            arrayOfLexicalsUnits.append(["INSTRUCTION", "AL"])

        elif (isString(text, i, "MI")):
            i += 2
            col += 2
            arrayOfLexicalsUnits.append(["INSTRUCTION", "MI"])

        elif (isString(text, i, "IN")):
            i += 2
            col += 2
            arrayOfLexicalsUnits.append(["INSTRUCTION", "IN"])

        elif (isString(text, i, "PS")):
            col += 2
            i += 2
            arrayOfLexicalsUnits.append(["INSTRUCTION", "PS"])

        elif (isString(text, i, "FT")):
            i += 2
            col += 2
            arrayOfLexicalsUnits.append(["INSTRUCTION", "FT"])

        elif (isString(text, i, "TT")):
            i += 2
            col += 2
            arrayOfLexicalsUnits.append(["INSTRUCTION_TEST", "TT"])

        elif (isString(text, i, "TH")):
            i += 2
            col += 2
            arrayOfLexicalsUnits.append(["INSTRUCTION", "TH"])

        elif (isString(text, i, "TV")):
            i += 2
            col += 2
            arrayOfLexicalsUnits.append(["INSTRUCTION", "TV"])
            
        elif (text[i] == " "):
            i += 1
            col += 2
            arrayOfLexicalsUnits.append(["SPACE", " "])
        elif (text[i] == "\n"):
            i += 1
            col = 0
            line += 1
            arrayOfLexicalsUnits.append(["END_LINE", "\n"])
        elif (text[i] in MOUVEMENT_LIST):
            arrayOfLexicalsUnits.append(["DIRECTION", text[i]])
            i += 1
            col += 1
        elif (text[i] == ";"):
            while (text[i] not in {'\n', '\0'}):
                i += 1
                col += 1
        else:
            raise InstructionSyntaxException(line, col, f"Unknow character {text[i]}")

    return arrayOfLexicalsUnits
