class Receptor:
    def __init__(self, datos):
        self.datos          = datos

    def recibir_datos(self):
        return self.datos
    
    def decodificar_datos(self, decodificador):
        data = decodificador.decodificador(self.datos)
        return data

    def decodificar_huffman(self):
        pass