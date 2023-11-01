class Emisor:
    def __init__(self, img, codificador):
        self.img = img
        self.codificador = codificador

    def enviar_paquetes(self):
        paquetes, dimensiones = self.codificador.codificar(self.img)
        return paquetes, dimensiones
    
    def codificar(self, codificador, datos):
        datos_codificados = codificador.codificar(datos)
        return datos_codificados
    
    
    # def enviar_paquetes_hufman(self):
    #     paquetes, dimensiones = self.codificador.codificar(self.img)
    #     return paquetes, dimensiones