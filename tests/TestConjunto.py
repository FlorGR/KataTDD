import unittest
from src.logica.Conjunto import Conjunto

class MyTestCase(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto=Conjunto([5])
        self.assertEqual(5,conjunto.promedio())