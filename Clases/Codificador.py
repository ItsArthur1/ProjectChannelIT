
from PIL import Image


class Codificador:
    def codificar(self, img_path):
        try:
            img = Image.open(img_path)
            pixel_data = list(img.getdata())
            binary_matrix = []
            current_byte = ''
            for pixel in pixel_data:
                binary_pixel = ''.join(format(component, '08b') for component in pixel)
                current_byte += binary_pixel
                while len(current_byte) >= 64:
                    binary_matrix.append(current_byte[:64])  
                    current_byte = current_byte[64:]
            print("Se codifico bien c:")
            return binary_matrix, img.size

        except Exception as e:
            print(f"Error: {e}")
            return None