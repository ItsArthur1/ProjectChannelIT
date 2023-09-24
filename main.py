from EsquemaComunicacion import Canal, Almacenamiento, Emisor, Receptor

if __name__ == "__main__":
    canal = Canal()

    carpeta_emisor = "./AlmacenamientoEmisor"
    almacenamiento_paquetes_emisor = Almacenamiento(f"{carpeta_emisor}/paquetes_emisor.bin")
    almacenamiento_imagen_emisor = Almacenamiento(f"{carpeta_emisor}/imagen_decodificada.jpg")
    
    carpeta_receptor = "./AlmacenamientoReceptor"
    almacenamiento_paquetes_receptor = Almacenamiento(f"{carpeta_receptor}/paquetes_receptor.bin")
    almacenamiento_imagen_receptor = Almacenamiento(f"{carpeta_receptor}/imagen_decodificada.jpg")

    emisor = Emisor("./AlmacenamientoEmisor/many-flowers.jpg", canal)

    imagen_original = emisor.cargar_imagen()
    alto, ancho, _ = imagen_original.shape
    paquetes = emisor.codificar_imagen(imagen_original, alto, ancho)
    
    for paquete in paquetes:
        almacenamiento_paquetes_emisor.guardar_paquete(paquete)
    
    emisor.enviar_datos(paquetes)

    receptor = Receptor(canal, almacenamiento_paquetes_receptor, almacenamiento_imagen_receptor)
    paquetes_recibidos = receptor.recibir_datos()
    
    for paquete in paquetes_recibidos:
        almacenamiento_paquetes_receptor.guardar_paquete(paquete)
    
    imagen_decodificada = receptor.decodificar_paquetes(paquetes_recibidos, alto, ancho)
    
    almacenamiento_imagen_emisor.guardar_imagen(imagen_decodificada)
    almacenamiento_imagen_receptor.guardar_imagen(imagen_decodificada)

    canal.calcular_entropias()
    for i, entropia in enumerate(canal.entropias):
        print(f"Entropía del paquete {i + 1}: {entropia:.2f} bits")
