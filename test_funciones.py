import unittest

from funciones import calcular_monto_plazo_fijo, calcular_monto_total, descontar_comision

class TestFunctions(unittest.TestCase):
    def test_calcular_monto_total(self):
        self.assertEqual(calcular_monto_total(10, 5), 80)
        self.assertEqual(calcular_monto_total(20, 3), 96)
        self.assertEqual(calcular_monto_total(15, 8), 192)

    def test_descontar_comision(self):
        self.assertEqual(descontar_comision(100, 0.1), 90)
        self.assertEqual(descontar_comision(200, 0.05), 190)
        self.assertEqual(descontar_comision(150, 0.2), 120)

    def test_calcular_monto_plazo_fijo(self):
        self.assertEqual(calcular_monto_plazo_fijo(1000), 1050)
        self.assertEqual(calcular_monto_plazo_fijo(500), 525)
        self.assertEqual(calcular_monto_plazo_fijo(2000), 2100)

if __name__ == '__main__':
    unittest.main()
