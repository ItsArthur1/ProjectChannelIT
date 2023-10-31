class Multiplexor:
    def __init__(self):
        self.canales = []
        self.datos_salvados = []

    def agregar_canal(self, canal):
        self.canales.append(canal)

    def transmitir_datos(self, datos):
        datos_restantes = datos
        while datos_restantes:
            for canal in self.canales:
                datos_transmitidos = canal.transmitir(datos_restantes)
                self.datos_salvados.extend(datos_transmitidos)
                datos_restantes = [dato for dato in datos_restantes if dato not in datos_transmitidos]
                if not datos_restantes:
                    print(f"Todos los datos han sido transmitidos exitosamente.")
                    return self.datos_salvados
        return self.datos_salvados
