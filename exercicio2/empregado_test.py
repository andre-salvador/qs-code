import unittest
from empregado import Empregado

class Test_calcular_reajuste(unittest.TestCase):
    
    def test_reajuste_string(self):
        p1 = Empregado()
        teste = Empregado.calcular_reajuste(self.salario)
        self.assertEquals(teste, 1575)


class Test_nome_completo(unittest.TestCase):
    def test_nome_completo(self):
        ...

class Test_validar_cargo(unittest.TestCase):
    def test_validar_cargo(self):
        ...