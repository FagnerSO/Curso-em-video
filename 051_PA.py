print('-'*8, 'Calculo Progressão Aritmética', '-'*8)

n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = n1 + (10-1) * razao

for i in range(n1, decimo + razao, razao):
    print(i, end='-')
print('Fim')

