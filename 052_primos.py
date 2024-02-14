print(' '*10, '\033[7;33mPesquisa Numeros Primos\033[m')

n1 = int(input('Digite o nunero a ser pesquisado: '))
c = 0

for i in range(1, n1 + 1):
    if n1 % i == 0:
        print('\033[33m\033[m', end=' ')
        c += 1
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end='')
if c == 2:
    print('\nÉ primo')
else:
    print('\nNão é primo')
