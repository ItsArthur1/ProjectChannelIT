import cv2
import numpy as np
import random
import time

class Canal:
    def __init__(self):
        self.paquetes = []

    def enviar_paquete(self, paquete):
        # Simula el envío del paquete a través del canal
        time.sleep(0.2)  # Simula un tiempo de transmisión de 100 ms
        self.paquetes.append(paquete)
        print("Paquete enviado")

    def recibir_paquete(self):
        if self.paquetes:
            # Simula la recepción de un paquete desde el canal
            print("Paquete recibido")
            return self.paquetes.pop(0)
        return None

class Almacenamiento:
    def __init__(self, filename):
        self.filename = filename

    def guardar_paquete(self, paquete):
        # Guarda un paquete en el almacenamiento (archivo)
        with open(self.filename, 'ab') as file:
            np.save(file, paquete)
        print(f"Paquete guardado en {self.filename}")

    def guardar_imagen(self, imagen):
        # Guarda una imagen decodificada en el almacenamiento
        cv2.imwrite(self.filename, imagen)
        print(f"Imagen guardada en {self.filename}")

class Emisor:
    def __init__(self, image_path, canal):
        self.image_path = image_path
        self.canal = canal

    def cargar_imagen(self):
        print("Cargando imagen...")
        return cv2.imread(self.image_path)

    def codificar_imagen(self, pixel_matrix, alto, ancho):
        paquetes = []

        for i in range(0, alto, alto):
            for j in range(0, ancho, ancho):
                paquete = pixel_matrix[i:i + alto, j:j + ancho]
                paquetes.append(paquete)

        print("Imagen codificada en paquetes")
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
        print("Todos los paquetes recibidos")
        return paquetes_recibidos

    def decodificar_paquetes(self, paquetes_recibidos, alto, ancho):
        paquetes_ajustados = [cv2.resize(paquete, (ancho, alto)) for paquete in paquetes_recibidos]

        if paquetes_ajustados:
            print("Paquetes decodificados y ajustados")
            return np.vstack([np.hstack(row) for row in paquetes_ajustados])
        else:
            print("No se recibieron paquetes válidos.")
            return None

    def guardar_imagen(self, imagen_decodificada):
        self.almacenamiento_imagen.guardar_imagen(imagen_decodificada)
        print(f"Imagen decodificada guardada en {self.almacenamiento_imagen.filename}")

