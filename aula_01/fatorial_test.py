import unittest
from fatorial import Fatorial

class Test_fatorial(unittest.TestCase):
    def test_fatorial_5(self):
        saida = Fatorial.fatorial(5)
        resultado = 120
        self.assertEquals(saida, resultado)
    
    def test_fatorial_6(self):
        saida = Fatorial.fatorial(6)
        resultado = 720
        self.assertEquals(saida, resultado)
    
    def test_fatorial_7(self):
        saida = Fatorial.fatorial(7)
        resultado = 5040
        self.assertEquals(saida, resultado)
    
    def test_fatorial_8(self):
        saida = Fatorial.fatorial(8)
        resultado = 40320
        self.assertEquals(saida, resultado)
    
    def test_fatorial_9(self):
        saida = Fatorial.fatorial(9)
        resultado = 362880
        self.assertEquals(saida, resultado)
    
    def test_fatorial_10(self):
        saida = Fatorial.fatorial(10)
        resultado = 3628800
        self.assertEquals(saida, resultado)
    
    def test_fatorial_11(self):
        saida = Fatorial.fatorial(11)
        resultado = 39916800
        self.assertEquals(saida, resultado)