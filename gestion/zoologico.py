class Zoologico:

    def __init__(self, nombre, ubicacion, zonas = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        if zonas is None:
            self._zonas = []
        else:
            self._zonas = zonas

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def  cantidadTotalAnimales(self):
        total = 0
        for zona in self._zonas:
            total += zona.cantidadAnimales()
        return total

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zonas

    def setZonas(self, zona):
        self._zonas = zona
