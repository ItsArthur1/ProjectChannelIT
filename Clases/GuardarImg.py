from PIL import Image

class GuardarImg:

    @staticmethod
    def guardar_imagen(pixel_data, dimensions, path):
        binary_data = ''.join(pixel_data)
        
        while len(binary_data) % 24 != 0:
            binary_data += '0'  # Asegurar que el binario sea múltiplo de 24 (RGB)

        if len(binary_data) / 24 != dimensions[0] * dimensions[1]:
            raise ValueError("La cantidad de datos binarios no coincide con las dimensiones de la imagen.")

        pixels = []

        for i in range(0, len(binary_data), 24):
            pixel_binary = binary_data[i:i+24]
            r = int(pixel_binary[:8], 2)
            g = int(pixel_binary[8:16], 2)
            b = int(pixel_binary[16:24], 2)
            pixels.append((r, g, b))

        img = Image.new("RGB", dimensions)
        img.putdata(pixels)
        img.save(path)
        print(f"Imagen guardada en {path}")
