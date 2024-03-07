print(f'\033[42m{" Extração de dados ":=^50}\033[m')
lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]: ')).upper().split()[0]
    if continua == 'N':
        break
print('-=' * 30)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} numeros')
print(f'A lista de forma decrescente é {lista}')
if 5 in lista:
    print(f'O numero 5 aparece na seguintes posições ', end='')
    for pos, c in enumerate(lista):
        if 5 == c:
            print(f'{pos}...', end=' ')
else:
    print('O numero 5 não consta nessa lista')
