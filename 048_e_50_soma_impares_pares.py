print('\n', '(_)'*5, '\033[31mSoma dos impares multiplo de 3\033[m', '(_)'*5, '\n')
s = 0
c = 0
for i  in range (1, 500):
    if i % 3 == 0 and i % 2 !=0:
       s = s + i
       c = c + 1
print(f'A soma de todos os numeros impares multiplos de 3 no intervalo de 1 a 500 é'
      f' \033[31m{s}\033[m')
print(f'Nesse intervalo foram somados \033[31m{c}\033[m números')

print('\n', '(_)'*5, '\033[31mSoma dos pares\033[m', '(_)'*5)
soma = 0
cont = 0

for i in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'A soma de todos os numeros pares digitados é \033[31m{soma}\033[m')
print(f'Nesse intervalo foram somados \033[31m{cont}\033[m números')