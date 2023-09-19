from .animal import Animal

class Pez(Animal):

    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas)->None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @staticmethod
    def crearBacalaos(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad