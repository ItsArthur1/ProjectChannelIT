class Nodo:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def es_hoja(self):
        return not (self.izquierda or self.derecha)

class Huffman:
    def __init__(self):
        self.codigos = {}
        self.inverso_codigos = {}

    def calcular_frecuencias(self, lista_datos):
        frecuencias = {}
        for dato in lista_datos:
            if dato in frecuencias:
                frecuencias[dato] += 1
            else:
                frecuencias[dato] = 1
        return frecuencias

    def construir_arbol(self, frecuencias):
        nodos = [Nodo(dato, freq) for dato, freq in frecuencias.items()]
        while len(nodos) > 1:
            nodos = sorted(nodos, key=lambda x: x.frecuencia)
            izquierda = nodos.pop(0)
            derecha = nodos.pop(0)
            nodo_interno = Nodo(None, izquierda.frecuencia + derecha.frecuencia)
            nodo_interno.izquierda = izquierda
            nodo_interno.derecha = derecha
            nodos.append(nodo_interno)
        return nodos[0]

    def construir_codigos(self, nodo, codigo_actual=""):
        if nodo is None:
            return
        if nodo.es_hoja():
            self.codigos[nodo.caracter] = codigo_actual
            self.inverso_codigos[codigo_actual] = nodo.caracter
        self.construir_codigos(nodo.izquierda, codigo_actual + "0")
        self.construir_codigos(nodo.derecha, codigo_actual + "1")

    def codificar(self, lista_datos):
        frecuencias = self.calcular_frecuencias(lista_datos)
        raiz = self.construir_arbol(frecuencias)
        self.construir_codigos(raiz)
        return [self.codigos[dato] for dato in lista_datos]

    def decodificador(self, lista_codificada):
        return [self.inverso_codigos[codigo] for codigo in lista_codificada]
