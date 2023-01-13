INSTRUCTION_LIST = []

def loadInstructions():
    """
    Zone de danger !
    """
    global INSTRUCTION_LIST

    from instruction.instructionList.dd import DD
    from instruction.instructionList.al import AL
    from instruction.instructionList.mi import MI
    from instruction.instructionList.inn import IN
    from instruction.instructionList.ps import PS
    from instruction.instructionList.ft import FT
    from instruction.instructionList.tt import TT
    from instruction.instructionList.th import TH
    from instruction.instructionList.tv import TV

    INSTRUCTION_LIST = {"DD": DD(), "AL": AL(), "MI": MI(), "IN": IN(), "PS": PS(), "FT": FT(), "TT": TT(), "TH": TH(), "TV": TV()}

MOUVEMENT_LIST = ["H", "B", "G", "D"]