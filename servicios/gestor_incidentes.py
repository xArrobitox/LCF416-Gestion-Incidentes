from modelos.incidente import Incidente

class GestorIncidentes:
    def __init__(self):
        self.incidentes = []
    def registrar(self, incidente):
        if not isinstance(incidente, Incidente):
            raise TypeError("Se requiere un objeto Incidente")
        if self.buscar(incidente.id) is not None:
            raise ValueError(f"ID duplicado: {incidente.id}")
        self.incidentes.append(incidente)
    def buscar(self, id):
        for i in self.incidentes:
            if i.id == id:
                return i
        return None
    def listar(self):
        return list(self.incidentes)
    def eliminar(self, id):
        i = self.buscar(id)
        if i is None: return False
        self.incidentes.remove(i)
        return True
    def cerrar_incidente(self, id):
        i = self.buscar(id)
        if i is None: return False
        i.cerrar()
        return True
    def clasificar_por_gravedad(self, gravedad):
        return [i for i in self.incidentes if i.gravedad == gravedad]
