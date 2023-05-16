import unittest
from empregado import Empregado

class Test_calcular_reajuste(unittest.TestCase):
    
    def test_reajuste_string_1500(self):
        p1 = Empregado('Carlos', 'Junior', 'diretor', 1500)
        saida = p1.calcular_reajuste()
        self.assertEquals(saida, 1575)
    
    def test_reajuste_string_15000(self):
        p1 = Empregado('Carlos', 'Junior', 'diretor', 15000)
        saida = p1.calcular_reajuste()
        self.assertEquals(saida, 15750)
    
    def test_reajuste_150000(self):
        p1 = Empregado('Carlos', 'Junior', 'diretor', 150000)
        saida = p1.calcular_reajuste()
        self.assertEquals(saida, 157500)


class Test_nome_completo(unittest.TestCase):
    
    def test_nome_completo(self):
        p1 = Empregado('Carlos', 'Junior', 'diretor', 15000)
        saida = p1.nome_completo()
        resultado = 'Carlos Junior'
        self.assertEquals(saida, resultado)
    
    def test_nome_completo_carlos(self):
        p1 = Empregado('Carlos', 'Marcos', 'diretor', 15000)
        saida = p1.nome_completo()
        resultado = 'Carlos Marcos'
        self.assertEquals(saida, resultado)
    
    def test_nome_completo_naldo(self):
        p1 = Empregado('Naldo', 'Ronaldo', 'diretor', 15000)
        saida = p1.nome_completo()
        resultado = 'Naldo Ronaldo'
        self.assertEquals(saida, resultado)
        

class Test_validar_cargo(unittest.TestCase):
    def test_validar_cargo(self):
        p1 = Empregado('Carlos', 'Junior', 'diretor', 15000)
        saida = p1.validar_cargo()
        resultado = 'Cargo existe na empresa'
        self.assertEquals(saida, resultado)
    
    def test_validar_cargo_chefe(self):
        p1 = Empregado('Carlos', 'Junior', 'diretor', 15000)
        saida = p1.validar_cargo()
        resultado = 'Esse cargo não está na empresa'
        self.assertEquals(saida, resultado)
    
    def test_validar_cargo_analista(self):
        p1 = Empregado('Carlos', 'Junior', 'diretor', 15000)
        saida = p1.validar_cargo()
        resultado = 'Cargo existe na empresa'
        self.assertEquals(saida, resultado)