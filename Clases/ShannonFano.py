class ShannonFano:
    
    def __init__(self):
        self.codigos = {}

    def dividir_lista(self, lista):
        total = sum(item[1] for item in lista)
        mitad = total / 2
        suma_actual = 0
        indice = 0
        for item in lista:
            if suma_actual + item[1] <= mitad:
                suma_actual += item[1]
                indice += 1
            else:
                break
        if indice == 0 or indice == len(lista):  # Asegurarnos de que no regrese la misma lista
            indice = len(lista) // 2
        return lista[:indice], lista[indice:]

    def codificar_recursivamente(self, lista, codigo_actual):
        if len(lista) == 1:
            self.codigos[lista[0][0]] = codigo_actual
            return
        lista1, lista2 = self.dividir_lista(lista)
        self.codificar_recursivamente(lista1, codigo_actual + '0')
        self.codificar_recursivamente(lista2, codigo_actual + '1')

    def codificar(self, datos):
        frecuencias = {}
        for dato in datos:
            if dato in frecuencias:
                frecuencias[dato] += 1
            else:
                frecuencias[dato] = 1
        lista_ordenada = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
        self.codificar_recursivamente(lista_ordenada, "")
        datos_codificados = [self.codigos[dato] for dato in datos]
        return datos_codificados

    def decodificador(self, datos_codificados):
        datos_decodificados = []
        codigo_inverso = {v: k for k, v in self.codigos.items()}
        for dato in datos_codificados:
            datos_decodificados.append(codigo_inverso[dato])
        return datos_decodificados
