class Calculadora:
    
    def adicao(x, y):
        if type(x) == str or type(y) == str:
            return 'Digite um número válido'
        return x + y
    
    def subtracao(x, y):
        if type(x) == str or type(y) == str:
            return 'Digite um número válido'
        return x - y

    def divisao(x, y):
        if type(x) == str or type(y) == str:
            return 'Digite um número válido'
        if y == 0:
            return 'Não da para dividir por 0'
        return x / y

    def multiplicacao(x, y):
        if type(x) == str or type(y) == str:
            return 'Digite um número válido'
        return x * y