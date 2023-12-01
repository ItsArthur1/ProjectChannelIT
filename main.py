from Clases.Emisor          import Emisor
from Clases.Codificador     import Codificador
from Clases.Decodificador   import Decodificador
from Clases.Almacenamiento  import Almacenamiento
from Clases.Canal           import Canal
from Clases.Multiplexor     import Multiplexor
from Clases.Receptor        import Receptor
from Clases.Entropia        import Entropia
from Clases.Huffman         import Huffman
from Clases.ShannonFano     import ShannonFano
from Clases.GuardarImg      import GuardarImg
from Clases.RLE             import RLE
from Clases.Inversa         import Inversa

def menu_principal():
    print("Seleccione el tipo de codificación:")
    print("1. Codificación Simple")
    print("2. Codificación Huffman")
    print("3. Codificación Shannon-Fano")
    print("4. RLE")
    print("5. Inversa")
    
    eleccion = input("Ingrese el número correspondiente a su elección: ")

    if eleccion == "1":
        normal()
    elif eleccion == "2":
        huffman()
    elif eleccion == "3":
        shannon_fano()
    elif eleccion == "4":
        rle()
    elif eleccion == "5":
        inversa()
    else:
        print("Opción no válida. Por favor, seleccione una opción correcta.")
        menu_principal()
        
        


def normal():
    # Sección del emisor
    emisor = Emisor("./img/descarga.jpg", Codificador())
    datos_codificados, size = emisor.enviar_paquetes()

    # Generar hashes de los datos codificados y crear diccionario de hashes
    hashes_datos = [emisor.generar_hash(dato) for dato in datos_codificados]
    diccionario_hashes = {hash_dato: dato for hash_dato, dato in zip(hashes_datos, datos_codificados)}

    # Sección de canal y multiplexor
    canal1 = Canal(id_canal=1)
    canal2 = Canal(id_canal=2)
    canal3 = Canal(id_canal=3)
    canal4 = Canal(id_canal=4)
    canal5 = Canal(id_canal=5)

    multiplexor = Multiplexor()
    multiplexor.agregar_canal(canal1)
    multiplexor.agregar_canal(canal2)
    multiplexor.agregar_canal(canal3)
    multiplexor.agregar_canal(canal4)
    multiplexor.agregar_canal(canal5)

    # Transmitir solo los hashes a través del multiplexor
    hashes_transmitidos = multiplexor.transmitir_datos(hashes_datos)
    print(f"Longitud original de los hashes: {len(hashes_datos)} y después del canal: {len(hashes_transmitidos)}")

    # Sección del receptor
    receptor = Receptor(hashes_transmitidos)

    # Utilizar la búsqueda binaria para encontrar los datos codificados correspondientes
    datos_recibidos = []
    for hash_dato in hashes_transmitidos:
        dato_decodificado = receptor.busqueda_binaria(hash_dato, diccionario_hashes)
        if dato_decodificado is not None:
            datos_recibidos.append(dato_decodificado)

    # Almacenar y procesar los datos recibidos
    almacenamiento_receptor = Almacenamiento(datos_recibidos)
    datos_receptor = almacenamiento_receptor.data

    # Guardar imagen decodificada
    guardar_img = GuardarImg().guardar_imagen(datos_receptor, size, "img.jpg")





def huffman():
    # Sección del emisor
    emisor = Emisor("./img/descarga.jpg", Codificador())
    datos, size = emisor.enviar_paquetes()    
    huffman = Huffman()
    datos_codificados = emisor.codificar(huffman, datos)

    # Generar hashes de los datos codificados y crear diccionario de hashes
    hashes_datos = [emisor.generar_hash(dato) for dato in datos_codificados]
    diccionario_hashes = {hash_dato: dato for hash_dato, dato in zip(hashes_datos, datos_codificados)}

    # Sección de canal y multiplexor
    canal1 = Canal(id_canal=1)
    canal2 = Canal(id_canal=2)
    canal3 = Canal(id_canal=3)
    canal4 = Canal(id_canal=4)
    canal5 = Canal(id_canal=5)

    multiplexor = Multiplexor()
    multiplexor.agregar_canal(canal1)
    multiplexor.agregar_canal(canal2)
    multiplexor.agregar_canal(canal3)
    multiplexor.agregar_canal(canal4)
    multiplexor.agregar_canal(canal5)

    # Transmitir solo los hashes a través del multiplexor
    hashes_transmitidos = multiplexor.transmitir_datos(hashes_datos)

    # Sección del receptor
    receptor = Receptor(hashes_transmitidos)

    # Utilizar la búsqueda binaria para encontrar los datos codificados correspondientes
    datos_recibidos = []
    for hash_dato in hashes_transmitidos:
        dato_decodificado = receptor.busqueda_binaria(hash_dato, diccionario_hashes)
        if dato_decodificado is not None:
            datos_recibidos.append(dato_decodificado)

    # Decodificar los datos recibidos con Huffman
    mensaje_decodificado = huffman.decodificador(datos_recibidos)

    # Verificar la correcta codificación y decodificación
    if datos == mensaje_decodificado:
        print("\n¡El mensaje fue codificado y decodificado correctamente!")
    else:
        print("\nHubo un error al decodificar el mensaje.")
        return 0

    # Guardar la imagen decodificada
    img = GuardarImg()
    img.guardar_imagen(mensaje_decodificado, size, "./img_codi.jpg")



    
    
def shannon_fano():
    # Sección del emisor
    emisor = Emisor("./img/descarga.jpg", Codificador())
    datos, size = emisor.enviar_paquetes()    
    shannon_fano = ShannonFano()
    datos_codificados = emisor.codificar(shannon_fano, datos)

    # Generar hashes de los datos codificados y crear diccionario de hashes
    hashes_datos = [emisor.generar_hash(dato) for dato in datos_codificados]
    diccionario_hashes = {hash_dato: dato for hash_dato, dato in zip(hashes_datos, datos_codificados)}

    # Sección de canal y multiplexor
    canal1 = Canal(id_canal=1)
    canal2 = Canal(id_canal=2)
    canal3 = Canal(id_canal=3)
    canal4 = Canal(id_canal=4)
    canal5 = Canal(id_canal=5)

    multiplexor = Multiplexor()
    multiplexor.agregar_canal(canal1)
    multiplexor.agregar_canal(canal2)
    multiplexor.agregar_canal(canal3)
    multiplexor.agregar_canal(canal4)
    multiplexor.agregar_canal(canal5)

    # Transmitir solo los hashes a través del multiplexor
    hashes_transmitidos = multiplexor.transmitir_datos(hashes_datos)

    # Sección del receptor
    receptor = Receptor(hashes_transmitidos)

    # Utilizar la búsqueda binaria para encontrar los datos codificados correspondientes
    datos_recibidos = []
    for hash_dato in hashes_transmitidos:
        dato_decodificado = receptor.busqueda_binaria(hash_dato, diccionario_hashes)
        if dato_decodificado is not None:
            datos_recibidos.append(dato_decodificado)

    # Decodificar los datos recibidos con Shannon-Fano
    mensaje_decodificado = shannon_fano.decodificador(datos_recibidos)

    # Verificar la correcta codificación y decodificación
    if datos == mensaje_decodificado:
        print("\n¡El mensaje fue codificado y decodificado correctamente!")    
    else:
        print("\nHubo un error al decodificar el mensaje.")
        return 0

    # Guardar la imagen decodificada
    img = GuardarImg()
    img.guardar_imagen(mensaje_decodificado, size, "./img_codi.jpg")

  
def rle():
    emisor = Emisor("./img/descarga.jpg", Codificador())
    datos, size = emisor.enviar_paquetes()    
    rle = RLE()
    datos_codificados = emisor.codificar(rle, datos)

    hashes_datos = [emisor.generar_hash(dato) for dato in datos_codificados]
    diccionario_hashes = {hash_dato: dato for hash_dato, dato in zip(hashes_datos, datos_codificados)}

    canal1 = Canal(id_canal=1)
    canal2 = Canal(id_canal=2)
    canal3 = Canal(id_canal=3)
    canal4 = Canal(id_canal=4)
    canal5 = Canal(id_canal=5)

    multiplexor = Multiplexor()
    multiplexor.agregar_canal(canal1)
    multiplexor.agregar_canal(canal2)
    multiplexor.agregar_canal(canal3)
    multiplexor.agregar_canal(canal4)
    multiplexor.agregar_canal(canal5)

    hashes_transmitidos = multiplexor.transmitir_datos(hashes_datos)

    receptor = Receptor(hashes_transmitidos)

    datos_recibidos = []
    for hash_dato in hashes_transmitidos:
        dato_decodificado = receptor.busqueda_binaria(hash_dato, diccionario_hashes)
        if dato_decodificado is not None:
            datos_recibidos.append(dato_decodificado)

    mensaje_decodificado = rle.decodificador(datos_recibidos)

    if datos == mensaje_decodificado:
        print("\n¡El mensaje fue codificado y decodificado correctamente!")    
    else:
        print("\nHubo un error al decodificar el mensaje.")
        return 0

    img = GuardarImg()
    img.guardar_imagen(mensaje_decodificado, size, "./img_codi.jpg")
  
  
  
 


def inversa():
    emisor = Emisor("./img/descarga.jpg", Codificador())
    datos, size = emisor.enviar_paquetes()    
    inversa = Inversa()
    datos_codificados = emisor.codificar(inversa, datos)

    hashes_datos = [emisor.generar_hash(dato) for dato in datos_codificados]
    diccionario_hashes = {hash_dato: dato for hash_dato, dato in zip(hashes_datos, datos_codificados)}

    canal1 = Canal(id_canal=1)
    canal2 = Canal(id_canal=2)
    canal3 = Canal(id_canal=3)
    canal4 = Canal(id_canal=4)
    canal5 = Canal(id_canal=5)

    multiplexor = Multiplexor()
    multiplexor.agregar_canal(canal1)
    multiplexor.agregar_canal(canal2)
    multiplexor.agregar_canal(canal3)
    multiplexor.agregar_canal(canal4)
    multiplexor.agregar_canal(canal5)

    hashes_transmitidos = multiplexor.transmitir_datos(hashes_datos)

    receptor = Receptor(hashes_transmitidos)

    datos_recibidos = []
    for hash_dato in hashes_transmitidos:
        dato_decodificado = receptor.busqueda_binaria(hash_dato, diccionario_hashes)
        if dato_decodificado is not None:
            datos_recibidos.append(dato_decodificado)

    mensaje_decodificado = inversa.decodificador(datos_recibidos)

    if datos == mensaje_decodificado:
        print("\n¡El mensaje fue codificado y decodificado correctamente!")    
    else:
        print("\nHubo un error al decodificar el mensaje.")
        return 0

    img = GuardarImg()
    img.guardar_imagen(mensaje_decodificado, size, "./img_codi.jpg")
  
  

  
    
    

# Iniciar el programa
if __name__ == "__main__":
    menu_principal()
