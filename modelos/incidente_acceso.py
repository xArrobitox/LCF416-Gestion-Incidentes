from modelos.incidente import Incidente

class IncidenteAcceso(Incidente):
    def __init__(self, id, descripcion, gravedad, usuario_afectado, intentos_detectados):
        super().__init__(id, descripcion, gravedad)
        if not isinstance(intentos_detectados, int) or intentos_detectados < 0:
            raise ValueError("Intentos debe ser entero no negativo")
        self.usuario_afectado = usuario_afectado
        self.intentos_detectados = intentos_detectados
    def generar_reporte(self):
        return f"{super().generar_reporte()} | Cuenta: {self.usuario_afectado} | Intentos: {self.intentos_detectados}"
