print(f'\033[7m{"Sequencia de Fibonacci":=^50}\033[m')

n = int(input('Digite o numero de elementos que deseja ser mostrado: '))
n1 = 0
n2 = 1
soma = 0
cont = 3
print('~'*30)
print(f'{n1}-{n2}', end='')
while cont <= n:
    n3 = n1 + n2
    print(f'-{n3}', end='')
    n1 = n2
    n2 = n3
    cont += 1
print('-FIM')