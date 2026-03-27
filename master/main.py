from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
import sys
import os

# Para que Python encuentre las carpetas
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from parser.DevOpsDSLLexer import DevOpsDSLLexer
from parser.DevOpsDSLParser import DevOpsDSLParser
from interpreter.interpreter import Interpreter
from executor.executor import Executor


def main():
    print("[INFO] Iniciando sistema DSL\n")

    # =========================
    # VALIDAR ARCHIVO
    # =========================
    file = "script.dsl"

    if len(sys.argv) > 1:
        file = sys.argv[1]

    if not os.path.exists(file):
        print(f"[ERROR] No existe el archivo: {file}")
        return

    # =========================
    # CARGAR DSL
    # =========================
    input_stream = FileStream(file)

    # =========================
    # LEXER (TOKENS)
    # =========================
    lexer = DevOpsDSLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    tokens.fill()

    print("========== TOKENS ==========")
    for token in tokens.tokens:
        if token.type != -1:
            print(f"{token.text} -> {token.type}")
    print()

    # =========================
    # PARSER (ÁRBOL)
    # =========================
    parser = DevOpsDSLParser(tokens)

    # 🔥 Manejo de errores sintácticos
    parser.removeErrorListeners()
    parser.addErrorListener(ConsoleErrorListener())

    tree = parser.program()

    print("========== ÁRBOL ==========")
    print(tree.toStringTree(recog=parser))
    print()

    # =========================
    # INTERPRETER + EXECUTOR
    # =========================
    executor = Executor()
    interpreter = Interpreter(executor)

    print("[INFO] Ejecutando DSL...\n")

    interpreter.visit(tree)

    print("\n[INFO] Ejecución finalizada")


if __name__ == "__main__":
    main()