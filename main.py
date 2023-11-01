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
    datos, size = emisor.enviar_paquetes()

    almacenamiento_emisor = Almacenamiento(datos)
    datos_emisor = almacenamiento_emisor.data


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

    datos_transmitidos = multiplexor.transmitir_datos(datos_emisor)
    print(f"la longitud original de los datos es: {len(datos_emisor)} y después del canal {len(datos_transmitidos)}")
    print(datos_transmitidos)

    # Sección de decodificar los datos del emisor que se mandaron del canal y guardar la imagen a partir de los datos decodificados
    receptor = Receptor(datos_transmitidos)
    datos_recibidos = receptor.recibir_datos()
    almacenamiento_receptor = Almacenamiento(datos_recibidos)
    datos_receptor = almacenamiento_receptor.data
    print(datos_receptor)
    codificar_datos = receptor.decodificar_datos(Decodificador())

    # Entropía
    entropia = Entropia()
    calcular_entropia = entropia.calcular_entropia(datos_receptor)
    print(f"La entropia es: {calcular_entropia}")

    guardar_img = GuardarImg().guardar_imagen(datos_recibidos, size, "img.jpg")


def huffman():
    emisor                  = Emisor("./img/descarga.jpg", Codificador())
    datos, size             = emisor.enviar_paquetes()    
    huffman                 = Huffman()
    datos_codificados       = emisor.codificar(huffman, datos)

    almacenamiento_emisor   = Almacenamiento(datos_codificados)
    mensaje_codificado      = almacenamiento_emisor.data
    
    # # Imprimir códigos Huffman
    # print("\nCódigos Huffman:")    
    
    # for caracter, codigo in huffman.codigos.items():
    #     print(f"'{caracter}': {codigo}")



    # Sección de canal y multiplexor
    canal1                  = Canal(id_canal=1)
    canal2                  = Canal(id_canal=2)
    canal3                  = Canal(id_canal=3)
    canal4                  = Canal(id_canal=4)
    canal5                  = Canal(id_canal=5)

    multiplexor             = Multiplexor()
    
    
    multiplexor.agregar_canal(canal1)
    multiplexor.agregar_canal(canal2)
    multiplexor.agregar_canal(canal3)
    multiplexor.agregar_canal(canal4)
    multiplexor.agregar_canal(canal5)

    datos_transmitidos      = multiplexor.transmitir_datos(mensaje_codificado)

    receptor                = Receptor(datos_transmitidos)
    
    mensaje_decodificado    = receptor.decodificar_datos(huffman)


    # Verificar que el mensaje decodificado sea igual al original
    if datos == mensaje_decodificado:
        print("\n¡El mensaje fue codificado y decodificado correctamente!")    
    else:
        print("\nHubo un error al decodificar el mensaje.")
        return 0
    
        
    img                     = GuardarImg()
    img.guardar_imagen(mensaje_decodificado, size, "./img_codi.jpg")
    
    
    
    
def shannon_fano():
    emisor                  = Emisor("./img/descarga.jpg", Codificador())
    datos, size             = emisor.enviar_paquetes()    
    shannon_fano            = ShannonFano()
    datos_codificados       = emisor.codificar(shannon_fano, datos)

    almacenamiento_emisor   = Almacenamiento(datos_codificados)
    mensaje_codificado      = almacenamiento_emisor.data
    
    # Sección de canal y multiplexor
    canal1                  = Canal(id_canal=1)
    canal2                  = Canal(id_canal=2)
    canal3                  = Canal(id_canal=3)
    canal4                  = Canal(id_canal=4)
    canal5                  = Canal(id_canal=5)

    multiplexor             = Multiplexor()
    
    
    multiplexor.agregar_canal(canal1)
    multiplexor.agregar_canal(canal2)
    multiplexor.agregar_canal(canal3)
    multiplexor.agregar_canal(canal4)
    multiplexor.agregar_canal(canal5)
    

    datos_transmitidos      = multiplexor.transmitir_datos(mensaje_codificado)

    receptor                = Receptor(datos_transmitidos)
    
    mensaje_decodificado    = receptor.decodificar_datos(shannon_fano)


    # Verificar que el mensaje decodificado sea igual al original
    if datos == mensaje_decodificado:
        print("\n¡El mensaje fue codificado y decodificado correctamente!")    
    else:
        print("\nHubo un error al decodificar el mensaje.")
        return 0
    
        
    img                     = GuardarImg()
    img.guardar_imagen(mensaje_decodificado, size, "./img_codi.jpg")
    
    
  
  
  
 
def rle():
    emisor                  = Emisor("./img/descarga.jpg", Codificador())
    datos, size             = emisor.enviar_paquetes()    
    rle                     = RLE()
    datos_codificados       = emisor.codificar(rle, datos)

    almacenamiento_emisor   = Almacenamiento(datos_codificados)
    mensaje_codificado      = almacenamiento_emisor.data
    
    # Sección de canal y multiplexor
    canal1                  = Canal(id_canal=1)
    canal2                  = Canal(id_canal=2)
    canal3                  = Canal(id_canal=3)
    canal4                  = Canal(id_canal=4)
    canal5                  = Canal(id_canal=5)

    multiplexor             = Multiplexor()
    
    
    multiplexor.agregar_canal(canal1)
    multiplexor.agregar_canal(canal2)
    multiplexor.agregar_canal(canal3)
    multiplexor.agregar_canal(canal4)
    multiplexor.agregar_canal(canal5)
    

    datos_transmitidos      = multiplexor.transmitir_datos(mensaje_codificado)

    receptor                = Receptor(datos_transmitidos)
    
    mensaje_decodificado    = receptor.decodificar_datos(rle)


    # Verificar que el mensaje decodificado sea igual al original
    if datos == mensaje_decodificado:
        print("\n¡El mensaje fue codificado y decodificado correctamente!")    
    else:
        print("\nHubo un error al decodificar el mensaje.")
        return 0
    
        
    img                     = GuardarImg()
    img.guardar_imagen(mensaje_decodificado, size, "./img_codi.jpg") 
  
  
  
  
 
def inversa():
    emisor                  = Emisor("./img/descarga.jpg", Codificador())
    datos, size             = emisor.enviar_paquetes()    
    inversa                 = Inversa()
    datos_codificados       = emisor.codificar(inversa, datos)

    almacenamiento_emisor   = Almacenamiento(datos_codificados)
    mensaje_codificado      = almacenamiento_emisor.data
    
    # Sección de canal y multiplexor
    canal1                  = Canal(id_canal=1)
    canal2                  = Canal(id_canal=2)
    canal3                  = Canal(id_canal=3)
    canal4                  = Canal(id_canal=4)
    canal5                  = Canal(id_canal=5)

    multiplexor             = Multiplexor()
    
    
    multiplexor.agregar_canal(canal1)
    multiplexor.agregar_canal(canal2)
    multiplexor.agregar_canal(canal3)
    multiplexor.agregar_canal(canal4)
    multiplexor.agregar_canal(canal5)
    

    datos_transmitidos      = multiplexor.transmitir_datos(mensaje_codificado)

    receptor                = Receptor(datos_transmitidos)
    
    mensaje_decodificado    = receptor.decodificar_datos(inversa)


    # Verificar que el mensaje decodificado sea igual al original
    if datos == mensaje_decodificado:
        print("\n¡El mensaje fue codificado y decodificado correctamente!")    
    else:
        print("\nHubo un error al decodificar el mensaje.")
        return 0
    
        
    img                     = GuardarImg()
    img.guardar_imagen(mensaje_decodificado, size, "./img_codi.jpg") 
  
  
  
  

  
    
    

# Iniciar el programa
if __name__ == "__main__":
    menu_principal()
