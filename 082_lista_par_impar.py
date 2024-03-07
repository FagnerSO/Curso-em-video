print(f'\033[42m{" Separação de listas ":=^50}\033[m')

lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um número: ')))
    continua = ' '
    while continua not in 'SN':
        continua = input('Deseja continuar [S/N]: ').upper().strip()[0]
    if continua == 'N':
        break

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de imapres é {impar}')
