class Receptor:
    def __init__(self, datos):
        self.datos          = datos

    def recibir_datos(self):
        return self.datos
    
    def decodificar_datos(self, decodificador):
        data = decodificador.decodificador(self.datos)
        return data
    
    def busqueda_binaria(self, hash_dato, diccionario_hashes):
        """
        Realiza una búsqueda binaria para encontrar el dato correspondiente al hash proporcionado.
        """
        claves = list(diccionario_hashes.keys())
        claves.sort()
        izquierda, derecha = 0, len(claves) - 1
        while izquierda <= derecha:
            medio = izquierda + (derecha - izquierda) // 2
            hash_medio = claves[medio]
            if hash_medio == hash_dato:
                return diccionario_hashes[hash_medio]
            elif hash_medio < hash_dato:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return None