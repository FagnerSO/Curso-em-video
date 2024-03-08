from pacote import moedas_109

n = float(input('Digite o preço: R$ '))

print(f'A metade de {moedas_109.moeda(n)} é {moedas_109.metade(n, True)}')
print(f'O dobro de {moedas_109.moeda(n)} é {moedas_109.dobro(n, True)}')
print(f'Aumentando em 10%, temos {moedas_109.aumento(n, 10, True)}')
print(f'Reduzindo 13%, temos {moedas_109.reducao(n, 13, True)}')