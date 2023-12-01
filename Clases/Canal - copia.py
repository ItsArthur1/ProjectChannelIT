import random

class Canal:
    def __init__(self, id_canal, probabilidad_ruido=0.8):
        self.id_canal = id_canal
        self.probabilidad_ruido = probabilidad_ruido

    def hay_ruido(self):
        return random.random() < self.probabilidad_ruido

    def transmitir(self, datos):
        if self.hay_ruido():
            print(f"Ruido detectado en el canal {self.id_canal}. Cambiando al siguiente canal.")
            return []
        else:
            print(f"Canal {self.id_canal} transmitió datos sin ruido.")
            return datos
