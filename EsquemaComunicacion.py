from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import numpy as np
import scipy.constants as const
import time

class Satelite:
    def tomar_foto(self, ruta):
        print("Tomando foto...")
        with open(ruta, "rb") as f:
            datos = f.read()
        return datos
    
    def encriptar_foto(self, datos, clave_aes):
        print("Encriptando foto...")
        cipher = AES.new(clave_aes, AES.MODE_CBC)
        iv = cipher.iv
        datos_encriptados = cipher.encrypt(pad(datos, AES.block_size))
        return datos_encriptados, iv

class AlmacenamientoEmisor:
    def __init__(self, velocidad):
        self.velocidad = velocidad
        self.datos_almacenados = []

    def almacenar(self, datos):
        print("Almacenando datos en el emisor...")
        time.sleep(len(datos) / self.velocidad)  # Simular tiempo de almacenamiento
        self.datos_almacenados.append(datos)

    def obtener_datos(self):
        return self.datos_almacenados.pop(0)

class AlmacenamientoReceptor:
    def __init__(self, velocidad):
        self.velocidad = velocidad
        self.datos_almacenados = []

    def almacenar(self, datos):
        print("Almacenando datos en el receptor...")
        time.sleep(len(datos) / self.velocidad)  # Simular tiempo de almacenamiento
        self.datos_almacenados.append(datos)

    def obtener_datos(self):
        return self.datos_almacenados.pop(0)

class CanalComunicacion:
    def __init__(self, velocidad, distancia, factor_ruido_cosmico, factor_ruido_galactico):
        self.velocidad = velocidad
        self.distancia = distancia
        self.factor_ruido_cosmico = factor_ruido_cosmico
        self.factor_ruido_galactico = factor_ruido_galactico

    def transmitir(self, datos):
        print("Transmitiendo datos por el canal...")
        tiempo_propagacion = self.distancia / const.speed_of_light
        tiempo_transmision = len(datos) / self.velocidad
        tiempo_total = tiempo_propagacion + tiempo_transmision
        datos_con_ruido = self.aplicar_ruido(datos)
        return datos_con_ruido

    def recibir(self, datos):
        print("Recibiendo datos por el canal...")
        time.sleep(len(datos) / self.velocidad)  # Simular tiempo de recepción
        return datos

    def aplicar_ruido(self, datos):
        datos_array = np.frombuffer(datos, dtype=np.uint8)
        ruido_cosmico = np.random.normal(0, self.factor_ruido_cosmico, len(datos_array))
        ruido_galactico = np.random.normal(0, self.factor_ruido_galactico, len(datos_array))
        datos_con_ruido = datos_array + ruido_cosmico + ruido_galactico
        datos_con_ruido = np.clip(datos_con_ruido, 0, 255).astype(np.uint8)
        return bytes(datos_con_ruido)

class Receptor:
    def __init__(self, canal, almacenamiento):
        self.canal = canal
        self.almacenamiento = almacenamiento

    def recibir(self, datos):
        datos_recibidos = self.canal.recibir(datos)
        return datos_recibidos

    def guardar_imagen_decodificada(self, ruta, datos_encriptados, clave_aes, iv):
        print("Guardando y decodificando imagen...")
        datos_desencriptados = self.desencriptar_foto(datos_encriptados, clave_aes, iv)
        self.almacenamiento.almacenar(datos_desencriptados)
        imagen = self.almacenamiento.obtener_datos()
        with open(ruta, "wb") as f:
            f.write(imagen)

    def desencriptar_foto(self, datos_encriptados, clave_aes, iv):
        cipher = AES.new(clave_aes, AES.MODE_CBC, iv=iv)
        datos_desencriptados = unpad(cipher.decrypt(datos_encriptados), AES.block_size)
        return datos_desencriptados
