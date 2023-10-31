class Decodificador:
    def decodificador(self, binary_matrix):

        try:
            binary_data = ''.join([str(item) for item in binary_matrix])  
            pixel_data = []

            for i in range(0, len(binary_data), 24):
                pixel_binary = binary_data[i:i+24]
                
                # Rellenar con ceros si pixel_binary no tiene 24 bits
                if len(pixel_binary) < 24:
                    pixel_binary = pixel_binary.ljust(24, '0')

                r = int(pixel_binary[:8], 2)
                g = int(pixel_binary[8:16], 2)
                b = int(pixel_binary[16:24], 2)
                pixel_data.append((r, g, b))
            print("Se decodifico bien c:")
            return pixel_data
        except Exception as e:
            print(f"Error al decodificar: {e}")
            return []
