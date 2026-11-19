from modelos.incidente import Incidente
from modelos.incidente_malware import IncidenteMalware
from modelos.incidente_acceso import IncidenteAcceso
from servicios.gestor_incidentes import GestorIncidentes

gestor = GestorIncidentes()
incidentes = [
    Incidente(1, "Equipo de demostracion", "Baja"),
    IncidenteMalware(2, "Archivo sospechoso", "Alta", "TroyanoDemo"),
    IncidenteAcceso(3, "Intentos fallidos", "Media", "cuenta_demo", 8),
    IncidenteMalware(4, "Proceso simulado", "Critica", "RansomwareDemo")
]
for incidente in incidentes:
    gestor.registrar(incidente)
for incidente in gestor.listar():
    print(incidente.generar_reporte())
