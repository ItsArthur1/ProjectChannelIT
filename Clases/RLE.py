class RLE:

    def __init__(self):
        pass

    def codificar(self, datos):
        if not datos:
            return []

        codificado = []
        
        for cadena in datos:
            sub_codificado = []
            i = 0
            while i < len(cadena):
                conteo = 1
                while (i + 1) < len(cadena) and cadena[i] == cadena[i + 1]:
                    i += 1
                    conteo += 1
                sub_codificado.append((cadena[i], conteo))
                i += 1
            codificado.append(sub_codificado)

        return codificado

    def decodificador(self, datos_codificados):
        if not datos_codificados:
            return []

        decodificado = []

        for sub_datos in datos_codificados:
            sub_decodificado = ""
            for elemento in sub_datos:
                caracter = elemento[0]
                conteo = elemento[1]
                sub_decodificado += caracter * conteo
            decodificado.append(sub_decodificado)

        return decodificado
