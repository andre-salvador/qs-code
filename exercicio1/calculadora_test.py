8import unittest
from calculadora import Calculadora

class Calculadora_test_adicao(unittest.TestCase):

    def test_adicao_string(self):
        x = 'b'
        y = 'a'
        teste = Calculadora.adicao(x,y)

        self.assertEquals(teste, 'Digite um número válido')
    
    def test_adicao_0_2(self):
        teste = Calculadora.adicao(x=0, y=2)
        resultado = 2

        self.assertEquals(teste, resultado)
    
    def test_adicao_12_5(self):
        teste = Calculadora.adicao(x=12, y=5)
        resultado = 17

        self.assertEquals(teste, resultado)
    
class Calculadora_test_subtracao(unittest.TestCase):

    def test_subtracao_string(self):
        x = 'b'
        y = 'a'
        teste = Calculadora.subtracao(x,y)

        self.assertEquals(teste, 'Digite um número válido')
    
    def test_subtracao_0_2(self):
        teste = Calculadora.subtracao(x=0, y=2)
        resultado = -2

        self.assertEquals(teste, resultado)
    
    def test_subtracao_12_5(self):
        teste = Calculadora.subtracao(x=12, y=5)
        resultado = 7

        self.assertEquals(teste, resultado)

class Calculadora_test_divisao(unittest.TestCase):

    def test_divisao_string(self):
        x = 'b'
        y = 'a'
        teste = Calculadora.divisao(x,y)
        resultado = 'Digite um número válido'

        self.assertEquals(teste, resultado)
    
    def test_divisao_0_2(self):
        teste = Calculadora.divisao(x=2, y=0)
        resultado = 'Não da para dividir por 0'

        self.assertEquals(teste, resultado)
    
    def test_divisao_12_5(self):
        teste = Calculadora.divisao(x=12, y=5)
        resultado = 2.4

        self.assertEquals(teste, resultado)
    
class Calculadora_test_multiplicacao(unittest.TestCase):

    def test_multiplicacao_string(self):
        x = 'b'
        y = 'a'
        teste = Calculadora.multiplicacao(x,y)

        self.assertEquals(teste, 'Digite um número válido')
    
    def test_multiplicacao_0_2(self):
        teste = Calculadora.multiplicacao(x=0, y=2)
        resultado = 0

        self.assertEquals(teste, resultado)
    
    def test_multiplicacao_12_5(self):
        teste = Calculadora.multiplicacao(x=12, y=5)
        resultado = 60

        self.assertEquals(teste, resultado)