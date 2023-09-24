import cv2
import numpy as np
import random
import time
from scipy.stats import entropy

class Canal:
    def __init__(self):
        self.paquetes = []
        self.entropias = []

    def enviar_paquete(self, paquete):
        # Simula el envío del paquete a través del canal
        # Aquí puedes agregar ruido al paquete
        probabilidad_ruido = 0.2  # 20% de probabilidad de que el paquete tenga ruido
        if random.random() < probabilidad_ruido:
            paquete = self.agregar_ruido(paquete)
        time.sleep(0.2)  # Simula un tiempo de transmisión de 100 ms
        self.paquetes.append(paquete)
        
    def agregar_ruido(self, paquete):
        # Aquí puedes agregar algún tipo de ruido al paquete
        # Por ejemplo, agregar ruido gaussiano
        ruido = np.random.normal(0, 25, paquete.shape).astype(np.uint8)
        paquete_con_ruido = cv2.add(paquete, ruido)
        return paquete_con_ruido

    def recibir_paquete(self):
        if self.paquetes:
            # Simula la recepción de un paquete desde el canal
            return self.paquetes.pop(0)
        return None

    def calcular_entropias(self):
        for paquete in self.paquetes:
            # Calcular la entropía del paquete y agregarla a la lista
            entropia = entropy(paquete.ravel(), base=2)
            self.entropias.append(entropia)

class Almacenamiento:
    def __init__(self, filename):
        self.filename = filename

    def guardar_paquete(self, paquete):
        # Guarda un paquete en el almacenamiento (archivo)
        with open(self.filename, 'ab') as file:
            np.save(file, paquete)

    def guardar_imagen(self, imagen):
        # Guarda una imagen decodificada en el almacenamiento
        cv2.imwrite(self.filename, imagen)

class Emisor:
    def __init__(self, image_path, canal):
        self.image_path = image_path
        self.canal = canal

    def cargar_imagen(self):
        return cv2.imread(self.image_path)

    def codificar_imagen(self, pixel_matrix, alto, ancho):
        paquetes = []

        for i in range(0, alto, alto):
            for j in range(0, ancho, ancho):
                paquete = pixel_matrix[i:i + alto, j:j + ancho]
                paquetes.append(paquete)
                
        return paquetes

    def enviar_datos(self, paquetes):
        for paquete in paquetes:
            self.canal.enviar_paquete(paquete)

class Receptor:
    def __init__(self, canal, almacenamiento_paquetes, almacenamiento_imagen):
        self.canal = canal
        self.almacenamiento_paquetes = almacenamiento_paquetes
        self.almacenamiento_imagen = almacenamiento_imagen

    def recibir_datos(self):
        paquetes_recibidos = []
        while True:
            paquete = self.canal.recibir_paquete()
            if paquete is None:
                break
            paquetes_recibidos.append(paquete)
        return paquetes_recibidos

    def decodificar_paquetes(self, paquetes_recibidos, alto, ancho):
        paquetes_ajustados = [cv2.resize(paquete, (ancho, alto)) for paquete in paquetes_recibidos]

        if paquetes_ajustados:
            return np.vstack([np.hstack(row) for row in paquetes_ajustados])
        else:
            print("No se recibieron paquetes válidos.")
            return None

    def guardar_imagen(self, imagen_decodificada):
        self.almacenamiento_imagen.guardar_imagen(imagen_decodificada)