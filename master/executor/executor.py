import subprocess
import os
from datetime import datetime
import random

class Executor:

    def __init__(self):
        self.groups = {
            "grupoA": ["nodo1", "nodo2"]
        }

    # =========================
    # EJECUTAR SCRIPT
    # =========================
    def run_on_node(self, node, script):
        script_path = f"nodes/{node}/cluster/scripts/{script}"
        log_path = f"nodes/{node}/cluster/logs/{script}.log"

        print(f"[EXEC] {node} -> {script}")

        if not os.path.exists(script_path):
            print(f"[ERROR] No existe el script: {script_path}")
            return

        result = subprocess.run(
            ["bash", script_path],
            capture_output=True,
            text=True
        )

        print(result.stdout)

        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        with open(log_path, "a") as f:
            f.write("=================================\n")
            f.write(f"Fecha: {datetime.now()}\n")
            f.write(result.stdout)
            f.write("\n")

    # =========================
    # GRUPO
    # =========================
    def update_group(self, group):
        for node in self.groups.get(group, []):
            self.run_on_node(node, "update.sh")

    # =========================
    # DEPLOY
    # =========================
    def deploy(self, app, group):
        print(f"[DEPLOY] {app} en {group}")
        for node in self.groups.get(group, []):
            self.run_on_node(node, "deploy.sh")

    # =========================
    # SENSORES SIMULADOS
    # =========================
    def get_sensor_data(self, node):
        return {
            "temp": random.randint(20, 60),
            "cpu": random.randint(10, 90)
        }