print(f'=' * 30)
print('      CADASTRO PRODUTOS       ')
print(f'=' * 30)

dados = {}
produtos = []
somapreco = 0
mediapreco = 0

while True:
    dados.clear()
    print()
    dados['codigo'] = input('Digite o código: ')
    dados['prod'] = str(input('Digite o produto: '))
    dados['preco'] = float(input('Digite o preço: R$'))
    produtos.append(dados.copy())

    somapreco += dados['preco']
    mediapreco = somapreco / len(produtos)

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
print(f'A valor médio dos produtos é R${mediapreco:5.2f}.')
print(f'Produtos com valor acima da média: ')
for p in produtos:
    if p['preco'] > mediapreco:
        print(f'• {p["prod"]}')