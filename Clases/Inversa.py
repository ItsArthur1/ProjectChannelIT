class Inversa:

    def __init__(self):
        pass

    def codificar(self, datos):
        if not datos:
            return []
        
        codificado = []

        for cadena in datos:
            # Invertir cada bit
            resultado = "".join('1' if bit == '0' else '0' for bit in cadena)
            codificado.append(resultado)

        return codificado

    def decodificador(self, datos_codificados):

        return self.codificar(datos_codificados)
