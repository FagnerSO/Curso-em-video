print(f'\033[1;32;7m{" ;) ":=^50}\033[m')
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'\033[31m{"=-" * 30:=^50}\033[m')
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for pos, c in enumerate(lista):
    if max(lista) == c:
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for pos, c in enumerate(lista):
    if min(lista) == c:
        print(f'{pos}...', end=' ')
