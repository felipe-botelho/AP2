print(f'=' * 30)
print('      CADASTRO PESSOAS       ')
print(f'=' * 30)

dados = {}
pessoa = []
somaidade = mediaidade = 0
somaaltura = mediaaltura = 0

while True:
    dados.clear()
    print()
    dados['codigo'] = int(input('Digite o código: '))
    dados['nome'] = str(input('Digite seu nome: '))
    dados['idade'] = int(input('Digite sua idade: '))
    dados['altura'] = float(input('Digite sua altura: '))
    pessoa.append(dados.copy())

    somaidade += dados['idade']
    mediaidade = somaidade / len(pessoa)
    somaaltura += dados['altura']
    mediaaltura = somaaltura / len(pessoa)

    while True:
        resposta = str(input('Deseja continuar cadastrando? (S | N) '))
        if resposta in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resposta == 'N':
        break

print()
print(f'=' * 30)
print('          RESULTADOS           ')
print(f'=' * 30)
print(f'Total de pessoas cadastradas: {len(pessoa)}')
print(f'A média das idades é {mediaidade} anos.')
print(f'A média das alturas é {mediaaltura:5.2f}m.')