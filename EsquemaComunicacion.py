from PIL import Image
import random
import time
import math
from collections import defaultdict, Counter
from heapq import heappush, heappop
from queue import PriorityQueue

# class Emisor:
#     def __init__(self, img, codificador):
#         self.img = img
#         self.codificador = codificador

#     def enviar_paquetes(self):
#         paquetes, dimensiones = self.codificador.codificar_data(self.img)
#         return paquetes, dimensiones

# class Canal:
#     def __init__(self, id_canal, probabilidad_ruido=0.2):
#         self.id_canal = id_canal
#         self.probabilidad_ruido = probabilidad_ruido

#     def hay_ruido(self):
#         return random.random() < self.probabilidad_ruido

#     def transmitir(self, datos):
#         if self.hay_ruido():
#             print(f"Ruido detectado en el canal {self.id_canal}. Cambiando al siguiente canal.")
#             return []
#         else:
#             print(f"Canal {self.id_canal} transmitió datos sin ruido.")
#             return datos

# class Multiplexor:
#     def __init__(self):
#         self.canales = []
#         self.datos_salvados = []

#     def agregar_canal(self, canal):
#         self.canales.append(canal)

#     def transmitir_datos(self, datos):
#         datos_restantes = datos.copy()
#         while datos_restantes:
#             for canal in self.canales:
#                 datos_transmitidos = canal.transmitir(datos_restantes)
#                 self.datos_salvados.extend(datos_transmitidos)
#                 datos_restantes = [dato for dato in datos_restantes if dato not in datos_transmitidos]
#                 if not datos_restantes:
#                     print(f"Todos los datos han sido transmitidos exitosamente.")
#                     return self.datos_salvados
#         return self.datos_salvados


# class Almacenamiento:
#     def __init__(self, data):
#         self.__data = data

#     @property
#     def data(self):
#         print("Guardando datos.....")
#         time.sleep(1)
#         return self.__data


# class Receptor:
#     def __init__(self, decodificador, datos, dimensiones, path):
#         self.decodificador  = decodificador
#         self.datos          = datos
#         self.dimensiones    = dimensiones
#         self.path           = path    

#     def recibir_datos(self):
#         return self.datos
    
#     def codificar_datos(self):
#         data = self.decodificador.decodificador(self.datos, self.dimensiones, self.path)
#         return data


# class Codificador:
#     def codificar_data(self, img_path):
#         try:
#             img = Image.open(img_path)
#             pixel_data = list(img.getdata())
#             binary_matrix = []
#             current_byte = ''
#             for pixel in pixel_data:
#                 binary_pixel = ''.join(format(component, '08b') for component in pixel)
#                 current_byte += binary_pixel
#                 while len(current_byte) >= 64:
#                     binary_matrix.append(current_byte[:64])  
#                     current_byte = current_byte[64:]

#             return binary_matrix, img.size

#         except Exception as e:
#             print(f"Error: {e}")
#             return None


# class Decodificador:
#     def decodificador(self, binary_matrix, dimensions, path):
#         try:
#             binary_data = ''.join([str(item) for item in binary_matrix])  
#             pixel_data = []
#             width, height = dimensions

#             for i in range(0, len(binary_data), 24):
#                 pixel_binary = binary_data[i:i+24]
#                 r = int(pixel_binary[:8], 2)
#                 g = int(pixel_binary[8:16], 2)
#                 b = int(pixel_binary[16:24], 2)
#                 pixel_data.append((r, g, b))

#             img = Image.new("RGB", (width, height))
#             img.putdata(pixel_data)
#             img.save(path)
#             print(f"Imagen guardada en {path}")

#         except Exception as e:
#             print(f"Error: {e}")



# class Nodo:
#     def __init__(self, valor, frecuencia):
#         self.valor = valor
#         self.frecuencia = frecuencia
#         self.izquierda = None
#         self.derecha = None

#     def __lt__(self, otro):
#         return self.frecuencia < otro.frecuencia
    
    
    
 
# class ArbolHuffman:
#     def __init__(self):
#         self.raiz = None
#         self.codigos = {}

#     def construir(self, datos):
#         frecuencias = Counter(datos)
#         cola_prioridad = PriorityQueue()
#         for valor, frecuencia in frecuencias.items():
#             nodo = Nodo(valor, frecuencia)
#             cola_prioridad.put(nodo)

#         while cola_prioridad.qsize() > 1:
#             nodo1 = cola_prioridad.get()
#             nodo2 = cola_prioridad.get()

#             nodo_combinado = Nodo(None, nodo1.frecuencia + nodo2.frecuencia)
#             nodo_combinado.izquierda = nodo1
#             nodo_combinado.derecha = nodo2

#             cola_prioridad.put(nodo_combinado)

#         self.raiz = cola_prioridad.get()

#     def _asignar_codigos_recursivo(self, nodo_actual, codigo_actual):
#         if nodo_actual is None:
#             return

#         if nodo_actual.valor is not None:
#             self.codigos[nodo_actual.valor] = codigo_actual
#             return

#         self._asignar_codigos_recursivo(nodo_actual.izquierda, codigo_actual + "0")
#         self._asignar_codigos_recursivo(nodo_actual.derecha, codigo_actual + "1")

#     def asignar_codigos(self):
#         self._asignar_codigos_recursivo(self.raiz, "")

#     def mostrar_codigos_comunes(self):
#         codigos_comunes = sorted(self.codigos.items(), key=lambda x: len(x[1]), reverse=True)
#         for i, (valor, codigo) in enumerate(codigos_comunes):
#             if i >= 5:  
#                 break
#             letra = chr(65 + i) 
#             print(f"{letra}: [{codigo}]")

#     def codificar(self, datos):
#         codificados = []
#         for caracter in datos:
#             if caracter in self.codigos:
#                 codificados.append(self.codigos[caracter])

#         return ''.join(codificados)

#     def decodificar(self, datos_codificados, dimensions, path):
#         nodo_actual = self.raiz
#         datos_decodificados = []
#         for bit in datos_codificados:
#             if nodo_actual is None:
#                 break

#             if bit == "0":
#                 nodo_actual = nodo_actual.izquierda
#             else:
#                 nodo_actual = nodo_actual.derecha

#             if nodo_actual.valor is not None:
#                 datos_decodificados.append(nodo_actual.valor)
#                 nodo_actual = self.raiz

#         self._guardar_imagen(datos_decodificados, dimensions, path)
#         return datos_decodificados

#     def _guardar_imagen(self, datos_binarios, dimensions, path):
#         binary_data = ''.join(datos_binarios)
#         pixel_data = []
#         width, height = dimensions

#         while len(binary_data) % 24 != 0:
#             binary_data += '0'  

#         for i in range(0, len(binary_data), 24):
#             pixel_binary = binary_data[i:i+24]
#             r = int(pixel_binary[:8], 2)
#             g = int(pixel_binary[8:16], 2)
#             b = int(pixel_binary[16:24], 2)
#             pixel_data.append((r, g, b))

#         img = Image.new("RGB", (width, height))
#         img.putdata(pixel_data)
#         img.save(path)
#         print(f"Imagen guardada en {path}")


# class NodoShannonFano:
#     def __init__(self, simbolo, frecuencia):
#         self.simbolo = simbolo
#         self.frecuencia = frecuencia
#         self.izquierda = None
#         self.derecha = None

# class ShannonFano:
#     def __init__(self):
#         self.codigos = {}

#     def construir_arbol(self, datos):
#         frecuencias = Counter(datos)
#         frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
#         simbolos, frecuencias = zip(*frecuencias_ordenadas)
#         self.raiz = self._construir_arbol(simbolos, frecuencias)
#         self._generar_codigos(self.raiz, "")

#     def _construir_arbol(self, simbolos, frecuencias):
#         if len(simbolos) == 1:
#             return NodoShannonFano(simbolos[0], frecuencias[0])

#         medio = len(simbolos) // 2
#         nodo_izquierda = self._construir_arbol(simbolos[:medio], frecuencias[:medio])
#         nodo_derecha = self._construir_arbol(simbolos[medio:], frecuencias[medio:])

#         nodo = NodoShannonFano(None, sum(frecuencias[:medio]))
#         nodo.izquierda = nodo_izquierda
#         nodo.derecha = nodo_derecha

#         return nodo

#     def _generar_codigos(self, nodo, codigo):
#         if nodo is None:
#             return

#         if nodo.simbolo is not None:
#             self.codigos[nodo.simbolo] = codigo
#             return

#         self._generar_codigos(nodo.izquierda, codigo + "0")
#         self._generar_codigos(nodo.derecha, codigo + "1")

#     def codificar(self, datos):
#         datos_codificados = ""
#         for simbolo in datos:
#             datos_codificados += self.codigos[simbolo]
#         return datos_codificados

#     def decodificar(self, datos_codificados):
#         datos_decodificados = ""
#         nodo_actual = self.raiz
#         for bit in datos_codificados:
#             if bit == "0":
#                 nodo_actual = nodo_actual.izquierda
#             else:
#                 nodo_actual = nodo_actual.derecha

#             if nodo_actual.simbolo is not None:
#                 datos_decodificados += nodo_actual.simbolo
#                 nodo_actual = self.raiz

#         return datos_decodificados

#     def guardar_imagen(self, datos_binarios, dimensions, path):
#         binary_data = ''.join(datos_binarios)
#         pixel_data = []
#         width, height = dimensions

#         while len(binary_data) % 24 != 0:
#             binary_data += '0'  

#         for i in range(0, len(binary_data), 24):
#             pixel_binary = binary_data[i:i+24]
#             r = int(pixel_binary[:8], 2)
#             g = int(pixel_binary[8:16], 2)
#             b = int(pixel_binary[16:24], 2)
#             pixel_data.append((r, g, b))

#         img = Image.new("RGB", (width, height))
#         img.putdata(pixel_data)
#         img.save(path)
#         print(f"Imagen guardada en {path}")






# class Entropia:
#     def calcular_entropia(self, datos):
#         entropia = 0
#         total_datos = len(datos)

#         if total_datos == 0:
#             return entropia

#         conteo = {}
#         for dato in datos:
#             if dato in conteo:
#                 conteo[dato] += 1
#             else:
#                 conteo[dato] = 1

#         for dato, frecuencia in conteo.items():
#             probabilidad = frecuencia / total_datos
#             entropia -= probabilidad * math.log2(probabilidad)

#         return entropia