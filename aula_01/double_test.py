import unittest
from double import Double

class Test_double(unittest.TestCase):
    def test_double_2(self):
        n = 2
        teste = Double.elevar(n)
        resultado = 4
        self.assertEquals(teste, resultado)
    
    def test_double_5(self):
        n = 5
        teste = Double.elevar(n)
        resultado = 25
        self.assertEquals(teste, resultado)
    
    def test_double_10(self):
        n = 10
        teste = Double.elevar(n)
        resultado = 100
        self.assertEquals(teste, resultado)