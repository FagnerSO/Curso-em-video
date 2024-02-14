print(f'\033[1:32m{"VAMOS JOGAR PAR OU IMPAR":=^50}\033[m')
from random import randint
cont = 0
while True:
    jogador = int(input('Escolha um número: '))
    pc = randint(0, 100)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o pc jogou {pc}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P' and total % 2 == 0:
        print('=-'*30)
        print('Voce VENCEU\nVamos Jogar Novamente...')
        print('=-' * 30)
    elif tipo == 'I' and total % 2 == 1:
        print('=-' * 30)
        print('Voce VENCEU\nVamos Jogar Novamente...')
        print('=-' * 30)
    else:
        print('=-' * 30)
        print('Voce perdeu!!')
        print('=-' * 30)
        break
    cont += 1
print(f'Fim de jogo! Voce venceu {cont} vezes.')