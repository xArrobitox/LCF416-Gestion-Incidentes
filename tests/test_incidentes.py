import unittest
from modelos.incidente import Incidente
from modelos.incidente_malware import IncidenteMalware
from modelos.incidente_acceso import IncidenteAcceso
from servicios.gestor_incidentes import GestorIncidentes

class Pruebas(unittest.TestCase):
    def test_T01_malware(self):
        self.assertIn("Troyano", IncidenteMalware(1,"Archivo","Alta","Troyano").generar_reporte())
    def test_T02_acceso(self):
        r=IncidenteAcceso(2,"Acceso","Media","cuenta_demo",5).generar_reporte()
        self.assertIn("cuenta_demo",r); self.assertIn("5",r)
    def test_T03_polimorfismo(self):
        xs=[Incidente(1,"Base","Baja"),IncidenteMalware(2,"Mal","Alta","Demo"),IncidenteAcceso(3,"Acc","Media","demo",2),IncidenteMalware(4,"Otro","Critica","X")]
        rs=[x.generar_reporte() for x in xs]
        self.assertEqual(len(rs),4); self.assertIn("Demo",rs[1]); self.assertIn("demo",rs[2])
    def test_T04_gravedad_invalida(self):
        x=Incidente(1,"X","Baja")
        with self.assertRaises(ValueError): x.gravedad="Urgente"
    def test_T05_estado(self):
        x=Incidente(1,"X","Baja"); x.cerrar(); self.assertEqual(x.estado,"Cerrado")
        x.reabrir(); self.assertEqual(x.estado,"Abierto")
    def test_T06_duplicado(self):
        g=GestorIncidentes(); g.registrar(Incidente(1,"X","Baja"))
        with self.assertRaises(ValueError): g.registrar(IncidenteMalware(1,"Y","Alta","Demo"))

if __name__=="__main__": unittest.main()
