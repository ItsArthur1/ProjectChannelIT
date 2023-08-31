from EsquemaComunicacion import Satelite, AlmacenamientoEmisor, AlmacenamientoReceptor, CanalComunicacion, Receptor
from Crypto.Random import get_random_bytes

# Simulación de una imagen (reemplaza esto con la ruta a tu imagen)
ruta_imagen = "./img/pic.jpg"

# Parámetros
clave_aes = get_random_bytes(16)
velocidad_canal = 1000000  # 1 Mbps
velocidad_almacenamiento_emisor = 100000000  # Velocidad de almacenamiento en bytes por segundo
velocidad_almacenamiento_receptor = 100000000  # Velocidad de almacenamiento en bytes por segundo
distancia = 300000000000  # 300,000 km
desviacion_estandar_ruido = 1000
factor_ruido_cosmico = 50  # Aumentar este valor para más ruido cósmico
factor_ruido_galactico = 20  # Aumentar este valor para más ruido galáctico


# Creación de objetos
satelite = Satelite()
almacenamiento_emisor = AlmacenamientoEmisor(velocidad_almacenamiento_emisor)
almacenamiento_receptor = AlmacenamientoReceptor(velocidad_almacenamiento_receptor)
canal = CanalComunicacion(velocidad_canal, distancia, factor_ruido_cosmico, factor_ruido_galactico)
receptor = Receptor(canal, almacenamiento_receptor)  # Se asigna el canal al receptor

# Flujo del esquema
datos_imagen = satelite.tomar_foto(ruta_imagen)
datos_encriptados, iv = satelite.encriptar_foto(datos_imagen, clave_aes)
almacenamiento_emisor.almacenar(datos_encriptados)
datos_transmitidos = canal.transmitir(almacenamiento_emisor.obtener_datos())
datos_recibidos = receptor.recibir(datos_transmitidos)

# Guardar la imagen decodificada
ruta_imagen_decodificada = "./almacenamiento/deco6.jpg"
receptor.guardar_imagen_decodificada(ruta_imagen_decodificada, datos_encriptados, clave_aes, iv)
