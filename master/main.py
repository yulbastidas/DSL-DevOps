from antlr4 import *
from parser.DevOpsDSLLexer import DevOpsDSLLexer
from parser.DevOpsDSLParser import DevOpsDSLParser
from interpreter.interpreter import Interpreter
from executor.executor import Executor

def main():
    print("[INFO] Iniciando sistema DSL\n")

    input_stream = FileStream("script.dsl")

    lexer = DevOpsDSLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    tokens.fill()

    print("========== TOKENS ==========")
    for token in tokens.tokens:
        if token.type != -1:
            print(f"{token.text} -> {token.type}")
    print()

    parser = DevOpsDSLParser(tokens)
    tree = parser.program()

    print("========== ÁRBOL ==========")
    print(tree.toStringTree(recog=parser))
    print()

    executor = Executor()
    interpreter = Interpreter(executor)

    interpreter.visit(tree)

if __name__ == "__main__":
    main()
