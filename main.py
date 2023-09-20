from EsquemaComunicacion import Canal, Almacenamiento, Emisor, Receptor

if __name__ == "__main__":
    canal = Canal()

    # Carpeta para el Emisor
    carpeta_emisor = "./AlmacenamientoEmisor"
    almacenamiento_paquetes_emisor = Almacenamiento(f"{carpeta_emisor}/paquetes_emisor.bin")

    
    # Carpeta para el Receptor
    carpeta_receptor = "./AlmacenamientoReceptor"
    almacenamiento_paquetes_receptor = Almacenamiento(f"{carpeta_receptor}/paquetes_receptor.bin")
    almacenamiento_imagen_receptor = Almacenamiento(f"{carpeta_receptor}/imagen_decodificada.jpg")

    # Emisor: Cambia la ruta de la imagen aquí
    emisor = Emisor("./AlmacenamientoEmisor/many-flowers.jpg", canal)  # Cambia "ruta_de_tu_imagen.jpg" por la ruta real de tu imagen

    imagen_original = emisor.cargar_imagen()
    alto, ancho, _ = imagen_original.shape
    paquetes = emisor.codificar_imagen(imagen_original, alto, ancho)
    
    # Guardar paquetes en la carpeta del Emisor
    for paquete in paquetes:
        almacenamiento_paquetes_emisor.guardar_paquete(paquete)
    
    # Emisor: Envía los paquetes al canal
    emisor.enviar_datos(paquetes)
    print("Datos enviados")

    # Receptor
    receptor = Receptor(canal, almacenamiento_paquetes_receptor, almacenamiento_imagen_receptor)
    paquetes_recibidos = receptor.recibir_datos()
    
    # Guardar paquetes en la carpeta del Receptor
    for paquete in paquetes_recibidos:
        almacenamiento_paquetes_receptor.guardar_paquete(paquete)
    
    imagen_decodificada = receptor.decodificar_paquetes(paquetes_recibidos, alto, ancho)
    
    # Guardar la imagen decodificada en la carpeta del Emisor y del Receptor

    almacenamiento_imagen_receptor.guardar_imagen(imagen_decodificada)
    print("Proceso de recepción y decodificación completado")