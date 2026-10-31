from modelos.usuario import Usuario
from modelos.incidente import Incidente
from servicios.gestor_incidentes import GestorIncidentes


def main():
    usuario1 = Usuario(1, "Ana Torres", "Analista")
    usuario2 = Usuario(2, "Luis Méndez", "Administrador")

    incidente1 = Incidente(101, "Correo sospechoso", "Alta")
    incidente2 = Incidente(102, "Acceso no autorizado", "Crítica")
    incidente3 = Incidente(103, "Alerta de malware en equipo", "Media")

    incidente1.asignar_responsable(usuario1)
    incidente2.asignar_responsable(usuario2)

    gestor = GestorIncidentes()

    gestor.registrar(incidente1)
    gestor.registrar(incidente2)
    gestor.registrar(incidente3)

    print("=== INCIDENTES REGISTRADOS ===")

    for incidente in gestor.listar():
        print(incidente.resumen())

    print("\n=== CIERRE DE INCIDENTE ===")
    gestor.cerrar_incidente(101)

    print("\n=== ESTADO ACTUAL ===")

    for incidente in gestor.listar():
        print(incidente.resumen())

    print("\n=== INCIDENTES DE ANA TORRES ===")

    for incidente in gestor.listar_por_responsable(usuario1):
        print(incidente.resumen())


if __name__ == "__main__":
    main()