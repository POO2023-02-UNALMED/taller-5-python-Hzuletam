from .animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas)->None:
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    @staticmethod
    def crearHalcones(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crearAguilas(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave( nombre, edad, "montanas", genero, "blanco y amarillo")

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self,color):
        self._colorPlumas = color
