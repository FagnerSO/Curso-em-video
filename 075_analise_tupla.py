tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),)
print(f'Os valores digitados foram {tupla}')
print(f'O número 9 aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O numero tres aparece pela primeira vez na posição {tupla.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os numeros pares foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
