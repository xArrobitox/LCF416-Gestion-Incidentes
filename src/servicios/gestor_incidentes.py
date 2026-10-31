from modelos.incidente import Incidente
from modelos.usuario import Usuario
from servicios.notificador import Notificador


class GestorIncidentes:
    def __init__(self):
        self.incidentes = []

    def registrar(self, incidente):
        if not isinstance(incidente, Incidente):
            raise TypeError("Debe registrar un incidente.")

        if self.buscar(incidente.id) is not None:
            return False

        self.incidentes.append(incidente)
        return True

    def listar(self):
        return self.incidentes

    def buscar(self, id):
        for incidente in self.incidentes:
            if incidente.id == id:
                return incidente
        return None

    def eliminar(self, id):
        incidente = self.buscar(id)

        if incidente is None:
            return False

        self.incidentes.remove(incidente)
        return True

    def listar_por_responsable(self, usuario):
        return [
            incidente for incidente in self.incidentes
            if incidente.responsable is usuario
        ]

    def clasificar_por_gravedad(self, gravedad):
        return [
            incidente for incidente in self.incidentes
            if incidente.gravedad.lower() == gravedad.lower()
        ]

    def contar_por_gravedad(self):
        conteo = {
            "Crítica": 0,
            "Alta": 0,
            "Media": 0,
            "Baja": 0
        }

        for incidente in self.incidentes:
            if incidente.gravedad in conteo:
                conteo[incidente.gravedad] += 1

        return conteo

    def cerrar_incidente(self, id):
        incidente = self.buscar(id)

        if incidente is None or incidente.estado == "Cerrado":
            return False

        incidente.cerrar()

        notificador = Notificador()
        notificador.notificar(
            f"El incidente {incidente.id} fue cerrado."
        )

        return True