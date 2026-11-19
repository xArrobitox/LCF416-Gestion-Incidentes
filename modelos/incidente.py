class Incidente:
    GRAVEDADES_PERMITIDAS = {"Baja", "Media", "Alta", "Critica"}
    def __init__(self, id, descripcion, gravedad):
        self.id = id
        self.descripcion = descripcion
        self.gravedad = gravedad
        self._estado = "Abierto"
    @property
    def gravedad(self):
        return self._gravedad
    @gravedad.setter
    def gravedad(self, valor):
        if valor not in self.GRAVEDADES_PERMITIDAS:
            raise ValueError("Gravedad no permitida")
        self._gravedad = valor
    @property
    def estado(self):
        return self._estado
    def cerrar(self):
        self._estado = "Cerrado"
    def reabrir(self):
        self._estado = "Abierto"
    def generar_reporte(self):
        return f"{self.id}: {self.descripcion} | Gravedad: {self.gravedad} | Estado: {self.estado}"
    def resumen(self):
        return self.generar_reporte()
