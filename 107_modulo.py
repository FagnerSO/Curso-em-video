from pacote import moedas_107

n = float(input('Digite o preço: R$ '))

print(f'A metade de {n} é {moedas_107.metade(n):.2f}')
print(f'O dobro de {n} é {moedas_107.dobro(n):.2f}')
print(f'Aumentando em 10%, temos {moedas_107.aumento(n, 10):.2f}')
print(f'Reduzindo 13%, temos {moedas_107.reducao(n, 13):.2f}')