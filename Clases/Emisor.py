import hashlib

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
    
    def generar_hash(self, dato):
        """
        Genera un hash SHA-256 para el dato proporcionado.
        """
        if isinstance(dato, str):
            dato = dato.encode('utf-8')
        elif not isinstance(dato, bytes):
            # Ajusta esta parte según la naturaleza de tus datos
            dato = str(dato).encode('utf-8')
        return hashlib.sha256(dato).hexdigest()
    
    def crear_diccionario_hashes(self, datos_codificados):
        """
        Crea un diccionario de hashes para los datos codificados.
        """
        diccionario_hashes = {}
        for dato in datos_codificados:
            hash_dato = self.generar_hash(dato)
            diccionario_hashes[hash_dato] = dato
        return diccionario_hashes