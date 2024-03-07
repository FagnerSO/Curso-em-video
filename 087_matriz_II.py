print(f'\033[42m{" Matriz II":=^50}\033[m')
matriz = [[], [], []]
soma = soma_coluna = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(valor)
        if valor % 2 == 0:
            soma += valor
        if j == 2:
            soma_coluna += valor
        if i == 1:
            if matriz[i][j] > maior:
                maior = matriz[i][j]
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]:^5} ]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna}.')
print(f'O maior valor da segunda linha é {maior}')
