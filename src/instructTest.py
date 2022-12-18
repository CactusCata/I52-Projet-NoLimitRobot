import instruction.instructLexicalAnalyser as instructLexicalAnalyser
import instruction.instructSyntaxAnalyser as instructSyntaxAnalyser

if __name__ == "__main__":
    text = "AL\nAL\nDD H\n"
    lexicalsUnits = instructLexicalAnalyser.analex(text)
    print(lexicalsUnits)
    instructSyntaxAnalyser.axiome(lexicalsUnits)