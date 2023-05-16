import unittest
from power import Power

class Test_power(unittest.TestCase):
    def test_power_2(self):
        n = 2
        x = 2
        teste = Power.elevar(n, x)
        resultado = 4
        self.assertEquals(teste, resultado)
    
    def test_power_5(self):
        n = 5
        x = 2
        teste = Power.elevar(n, x)
        resultado = 25
        self.assertEquals(teste, resultado)
    
    def test_power_10(self):
        n = 10
        x = 2
        teste = Power.elevar(n, x)
        resultado = 100
        self.assertEquals(teste, resultado)
    
    def test_power_15(self):
        n = 15
        x = 2
        teste = Power.elevar(n, x)
        resultado = 225
        self.assertEquals(teste, resultado)
    
    def test_power_20(self):
        n = 20
        x = 2
        teste = Power.elevar(n, x)
        resultado = 400
        self.assertEquals(teste, resultado)