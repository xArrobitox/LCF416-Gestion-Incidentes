from modelos.usuario import Usuario
from modelos.incidente import Incidente
from servicios.gestor_incidentes import GestorIncidentes


def main():
    usuario1 = Usuario(1, "Ana Torres", "Analista")
    usuario2 = Usuario(2, "Luis Méndez", "Administrador")

    incidente1 = Incidente(101, "Correo sospechoso", "Alta")
    incidente2 = Incidente(102, "Acceso no autorizado", "Crítica")
    incidente3 = Incidente(103, "Alerta de malware", "Media")
    incidente4 = Incidente(104, "Intento de phishing", "Alta")
    incidente5 = Incidente(105, "Robo de credenciales", "Crítica")
    incidente6 = Incidente(106, "Software desactualizado", "Baja")

    incidente1.asignar_responsable(usuario1)
    incidente2.asignar_responsable(usuario2)
    incidente4.asignar_responsable(usuario1)

    gestor = GestorIncidentes()

    print("=== REGISTRO DE INCIDENTES ===")

    for incidente in [
        incidente1, incidente2, incidente3,
        incidente4, incidente5, incidente6
    ]:
        print(f"Incidente {incidente.id}: {gestor.registrar(incidente)}")

    print("\n=== INTENTO DE REGISTRO DUPLICADO ===")
    print(gestor.registrar(incidente1))

    print("\n=== INCIDENTES REGISTRADOS ===")

    for incidente in gestor.listar():
        print(incidente.resumen())

    print("\n=== CLASIFICACIÓN POR GRAVEDAD ===")

    for gravedad in ["Crítica", "Alta", "Media", "Baja"]:
        incidentes = gestor.clasificar_por_gravedad(gravedad)
        print(f"{gravedad}: {len(incidentes)} incidente(s)")

    print("\n=== CONTEO DE INCIDENTES ===")

    for gravedad, cantidad in gestor.contar_por_gravedad().items():
        print(f"{gravedad}: {cantidad}")

    print("\n=== ELIMINACIÓN DE UN INCIDENTE ===")
    gestor.eliminar(103)
    print(f"Incidentes registrados: {len(gestor.listar())}")
    print(f"El objeto eliminado todavía existe: {incidente3.resumen()}")

    print("\n=== CIERRE DE INCIDENTE ===")
    gestor.cerrar_incidente(101)

    print("\n=== INCIDENTES DE ANA TORRES ===")

    for incidente in gestor.listar_por_responsable(usuario1):
        print(incidente.resumen())


if __name__ == "__main__":
    main()