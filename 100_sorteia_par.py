from time import sleep
from random import randint
lista = []
def sorteia(num):
    print(f'Sorteando {num} valores da lista: ', end='')
    for i in range(num):
        lista.append(randint(1, 10))
        print(lista[i], end=' ')
    print('PRONTO !')


def soma(lista):
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    print(f'Somando os valores pares de {lista}, temos {s}')

sorteia(int(input('Quantos números deseja sortear: ')))
soma(lista)


