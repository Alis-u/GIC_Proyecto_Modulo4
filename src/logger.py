from datetime import datetime

class LoggerSistema:

    def __init__(self, archivo="logs.txt"):
        self.archivo = archivo

    def registrar_evento(self, mensaje):
        with open(self.archivo, "a", encoding="utf-8") as f:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{fecha}] EVENTO: {mensaje}\n")

    def registrar_error(self, mensaje):
        with open(self.archivo, "a", encoding="utf-8") as f:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{fecha}] ERROR: {mensaje}\n")
