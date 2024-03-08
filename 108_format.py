from pacote import moedas_108

n = float(input('Digite o preço: R$ '))

print(f'A metade de {moedas_108.moeda(n)} é {moedas_108.moeda(moedas_108.metade(n))}')
print(f'O dobro de {moedas_108.moeda(n)} é {moedas_108.moeda(moedas_108.dobro(n))}')
print(f'Aumentando em 10%, temos {moedas_108.moeda(moedas_108.aumento(n, 10))}')
print(f'Reduzindo 13%, temos {moedas_108.moeda(moedas_108.reducao(n, 13))}')