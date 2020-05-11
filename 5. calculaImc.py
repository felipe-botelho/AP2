from imc import Pessoa

print(f'=' * 30)
print('          CÁLCULO IMC        ')
print(f'=' * 30)
nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

p1 = Pessoa(nome,idade,peso,altura)

p1.calculaIMC()
p1.imprimeIMC()