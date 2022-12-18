class InstructionSyntaxException(Exception):

    def __init__(self, line, col, message):
        self.line = line
        self.col = col
        self.message = message

    def __str__(self):
        return f"Syntax error on {self.getErrorEmplacement}: {self.message}"

    def getErrorEmplacement(self):
        return (self.line, self.col)
