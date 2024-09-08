import unittest
from termo_formado import MaquinaTermoformado

class TestMaquinaTermoformado(unittest.TestCase):

    def setUp(self):
        self.maquina = MaquinaTermoformado()

    def test_temperatura_ambiente_no_supera_optima(self):

        self.maquina.calentar()
        self.assertLessEqual(self.maquina._MaquinaTermoformado__temperatura_actual, self.maquina._MaquinaTermoformado__temperatura_optima)

    def test_temperatura_optima_mayor_a_actual(self):
        self.maquina._MaquinaTermoformado__set_temperatura_actual(140)
        self.maquina._MaquinaTermoformado__set_temperatura_optima(130)
        self.assertEqual(self.maquina._MaquinaTermoformado__temperatura_optima, 150)

    def test_asignar_material_negativo(self):

        self.maquina._MaquinaTermoformado__set_material_disponible(-500)
        self.assertEqual(self.maquina._MaquinaTermoformado__material_disponible, 1000)

    def test_formar_lote_exitoso(self):

        self.maquina._MaquinaTermoformado__set_temperatura_actual(150)
        self.maquina.formar(100)
        self.assertEqual(self.maquina._MaquinaTermoformado__material_disponible, 900)

    def test_formar_lote_falla_temperatura_baja(self):

        self.maquina.formar(100)
        self.assertEqual(self.maquina._MaquinaTermoformado__material_disponible, 1000)

    def test_formar_lote_falla_material_insuficiente(self):
        self.maquina._MaquinaTermoformado__set_temperatura_actual(150)
        self.maquina.formar(1500)
        self.assertEqual(self.maquina._MaquinaTermoformado__material_disponible, 1000)


if __name__ == '__main__':
    unittest.main()
