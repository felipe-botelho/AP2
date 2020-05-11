print(f'=' * 30)
print('       SISTEMA DE CADASTRO        ')
print(f'=' * 30)

while True:

    nome = input('Digite o nome a ser cadastrado: ')
    telefone = input('Digite o telefone a ser cadastrado: ')
    arquivo = open('dados.txt', 'a')
    arquivo.write(f'Nome cadastrado: {nome} \nTelefone de {nome}: {telefone} \n\n')
    print(f'{arquivo.name} atualizado! \n')
    arquivo.close()

    while True:
        resposta = str(input('Deseja continuar cadastrando? (S | N) '))
        if resposta in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resposta == 'N':
        break

print('\n')
print(f'Operação concluída com sucesso no arquivo {arquivo.name}')
print('\n')
print(f'=' * 30)
print('       DADOS CADASTRADOS        ')
print(f'=' * 30)
arquivo = open('dados.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo = open('dados.txt', 'w')
arquivo.close()
