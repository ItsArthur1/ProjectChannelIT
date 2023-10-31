import time

class Almacenamiento:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        print("Guardando datos.....")
        time.sleep(1)
        return self.__data
