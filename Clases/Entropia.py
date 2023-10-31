import math

class Entropia:
    def calcular_entropia(self, datos):
        entropia = 0
        total_datos = len(datos)

        if total_datos == 0:
            return entropia

        conteo = {}
        for dato in datos:
            if dato in conteo:
                conteo[dato] += 1
            else:
                conteo[dato] = 1

        for dato, frecuencia in conteo.items():
            probabilidad = frecuencia / total_datos
            entropia -= probabilidad * math.log2(probabilidad)

        return entropia