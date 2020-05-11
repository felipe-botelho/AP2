class Pessoa(object):
    def __init__(self,n, i, p, a):
        self.nome = n
        self.idade = i
        self.peso = p
        self.altura = a
        self.imc = 0
        self.resultado = 0

    def calculaIMC(self):
        self.imc = self.peso/(self.altura*self.altura)
        if self.imc < 18.5:
            self.resultado = "Abaixo do peso"
        elif self.imc > 18.5 and self.imc < 24.9:
            self.resultado = "Peso normal"
        elif self.imc > 24.9 and self.imc < 29.9:
            self.resultado = "Sobrepeso"
        elif self.imc > 29.9 and self.imc < 34.9:
            self.resultado = "Obesidade Grau 1"
        elif self.imc > 34.9 and self.imc < 39.9:
            self.resultado = "Obesidade Grau 2"
        else:
            self.resultado = "Obesidade Grau 3"
        return self.imc

    def imprimeIMC(self):
        print()
        print(f'=' * 30)
        print('       DADOS CADASTRADOS      ')
        print(f'=' * 30)
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade} anos')
        print(f'Peso: {self.peso}KG')
        print(f'Altura: {self.altura}m')
        print()
        print(f'=' * 30)
        print('         RESULTADO IMC       ')
        print(f'=' * 30)
        print(f'O IMC do {self.nome} é {self.calculaIMC():5.2f} e ele está no estágio {self.resultado}.')