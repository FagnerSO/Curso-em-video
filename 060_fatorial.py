print('|'*10, 'Fatorial com while', '|'*10)

fatorial = int(input('Digite o valor a ser fatorado: '))
c = fatorial - 1

while c != 0:
    fatorial = fatorial * c
    c -= 1
print(f'O resultado é {fatorial}')

print('|'*10, 'Fatorial com for', '|'*10)

fatorial = int(input('Digite o valor a ser fatorado: '))

for i in range(fatorial - 1, 0, -1):
    fatorial = fatorial * i
print(f'O resultado é {fatorial}')
