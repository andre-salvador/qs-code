class Empregado:
    def init(nome, sobrenome, cargo, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.salario = 1500
        self.taxa = 1.05

    def calcular_reajuste(self):
        reajuste = self.salario * self.taxa

        return reajuste

    def nome_completo(self):
        return self.nome + self.sobrenome

    def validar_cargo(self):
        lista = ['presidente', 'diretor', 'gerente', 'analista', 'auxiliar']

        for i in lista:
            if i == self.cargo:
                return 'Cargo existe na empresa'
            
        return 'Esse cargo não está na empresa'