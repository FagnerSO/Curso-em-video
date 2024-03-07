print(f'\033[1;32;7m{" MEGASENA ":=^50}\033[m')
from random import randint
from time import sleep
lista = []
interna = []
jogos = int(input('Quantos jogos deseja fazer: '))
print('-=' * 30)
for i in range(0, jogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in interna:
            interna.append(num)
            cont += 1
        if cont >= 6:
            break
    interna.sort()
    lista.append(interna[:])
    interna.clear()
    print(f'\033[4{i}m Jogo {i + 1}: {lista[i]}\033[m')
    sleep(0.5)
print('-=' * 5, 'BOA SORTE', '-=' * 5)

