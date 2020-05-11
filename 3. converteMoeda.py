from conversorMoeda import conversor
from brcurrency.dolar import Dolar
from brcurrency.libra import Libra
from brcurrency.euro import Euro

dolar =  Dolar()
d = dolar.get_cotacao()

libra = Libra()
l = libra.get_cotacao()

euro = Euro()
e = euro.get_cotacao()

print(f'=' * 30)
print('      CONVERSOR DE MOEDAS       ')
print(f'=' * 30)

moeda = float(input('Digite um valor: R$'))

print()
print(f'=' * 30)
print('          RESULTADOS           ')
print(f'=' * 30)
print(f'Valor em real: R${moeda}')
print(f'Valor em dólar: ${conversor.conv(moeda, d):5.2f}')
print(f'Valor em euro: €{conversor.conv(moeda, e):5.2f}')
print(f'Valor em libra: £{conversor.conv(moeda, l):5.2f}')