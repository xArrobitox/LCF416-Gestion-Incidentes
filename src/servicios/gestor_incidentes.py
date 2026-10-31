from modelos.incidente import Incidente
from modelos.usuario import Usuario
from servicios.notificador import Notificador


class GestorIncidentes:
    def __init__(self):
        self.incidentes = []

    def registrar(self, incidente):
        self.incidentes.append(incidente)

    def listar(self):
        return self.incidentes

    def buscar(self, id):
        for incidente in self.incidentes:
            if incidente.id == id:
                return incidente
        return None

    def listar_por_responsable(self, usuario):
        return [
            incidente for incidente in self.incidentes
            if incidente.responsable is usuario
        ]

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