class Usuario:
    def __init__(self, id, nombre, rol):
        self.id = id
        self.nombre = nombre
        self.rol = rol

    def resumen(self):
        return f"Usuario {self.id}: {self.nombre} ({self.rol})"