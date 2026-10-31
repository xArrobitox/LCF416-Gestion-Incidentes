from modelos.usuario import Usuario


class Incidente:
    def __init__(self, id, descripcion, gravedad):
        self.id = id
        self.descripcion = descripcion
        self.gravedad = gravedad
        self.estado = "Abierto"
        self.responsable = None

    def asignar_responsable(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("El responsable debe ser un usuario.")
        self.responsable = usuario

    def quitar_responsable(self):
        self.responsable = None

    def cerrar(self):
        self.estado = "Cerrado"

    def resumen(self):
        nombre = self.responsable.nombre if self.responsable else "Sin asignar"
        return (
            f"Incidente {self.id} | {self.descripcion} | "
            f"Gravedad: {self.gravedad} | Estado: {self.estado} | "
            f"Responsable: {nombre}"
        )