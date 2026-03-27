from parser.DevOpsDSLVisitor import DevOpsDSLVisitor
from datetime import datetime
import threading

class Interpreter(DevOpsDSLVisitor):

    def __init__(self, executor):
        self.executor = executor

    # =========================
    # PROGRAMA PRINCIPAL
    # =========================
    def visitProgram(self, ctx):
        print("[INFO] Ejecutando DSL...\n")

        try:
            for stmt in ctx.statement():
                self.visit(stmt)
        except Exception as e:
            print(f"[ERROR GLOBAL] {e}")

    # =========================
    # NODO
    # =========================
    def visitNodeCommand(self, ctx):
        node = ctx.ID().getText()
        script = ctx.STRING().getText().strip('"')

        if not script.endswith(".sh"):
            print(f"[ERROR] Script inválido: {script}")
            return

        print(f"[DSL] {node}.run({script})")
        print(f"[LOG] {datetime.now()} -> Ejecutando {node}.{script}")

        self.executor.run_on_node(node, script)

    # =========================
    # GRUPO
    # =========================
    def visitGroupCommand(self, ctx):
        group = ctx.ID().getText()

        print(f"[DSL] {group}.update()")
        print(f"[LOG] {datetime.now()} -> Ejecutando update en {group}")

        self.executor.update_group(group)

    # =========================
    # DEPLOY
    # =========================
    def visitDeployCommand(self, ctx):
        app = ctx.ID(0).getText()
        group = ctx.ID(1).getText()

        print(f"[DSL] deploy {app} to {group}")
        print(f"[LOG] {datetime.now()} -> Deploy {app} en {group}")

        self.executor.deploy(app, group)

    # =========================
    # PARALELO
    # =========================
    def visitParallelBlock(self, ctx):
        print("[DSL] Ejecutando en paralelo")

        threads = []

        for stmt in ctx.statement():
            t = threading.Thread(target=self.safe_execute, args=(stmt,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    # =========================
    # STATUS (SENSORES)
    # =========================
    def visitStatusCommand(self, ctx):
        node = ctx.ID().getText()
        data = self.executor.get_sensor_data(node)

        print(f"[DSL] {node}.status()")
        print(f"[STATUS] {node} -> CPU: {data['cpu']}% | TEMP: {data['temp']}°C")

    # =========================
    # EJECUCIÓN SEGURA
    # =========================
    def safe_execute(self, stmt):
        try:
            self.visit(stmt)
        except Exception as e:
            print(f"[ERROR THREAD] {e}")