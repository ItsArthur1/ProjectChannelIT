class Emisor:
    def __init__(self, img, codificador):
        self.img = img
        self.codificador = codificador

    def enviar_paquetes(self):
        paquetes, dimensiones = self.codificador.codificar(self.img)
        return paquetes, dimensiones
    
    def codificar_huffman(self, Huffman, datos):
        datos_codificados = Huffman.codificar(datos)
        return datos_codificados
    
    
    # def enviar_paquetes_hufman(self):
    #     paquetes, dimensiones = self.codificador.codificar(self.img)
    #     return paquetes, dimensiones