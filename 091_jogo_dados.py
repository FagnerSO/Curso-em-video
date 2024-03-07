from random import randint
from time import sleep
print('Valores sorteados')
jogadores = {}
geral = []
for i in range(1, 5):
    jogadores['jogador'] = i
    jogadores['dado'] = randint(1, 6)
    geral.append(jogadores.copy())
    print(f'O jogador {geral[i - 1]["jogador"]}, tirou {geral[i - 1]["dado"]}')
    sleep(0.2)
print('-=' * 30)
print('Ranking dos jogadores')
ordenada = sorted(geral, key=lambda x: x['dado'], reverse=True)

for l in range(1, 5):
    print(f'{l}ª lugar: Jogador {ordenada[l-1]["jogador"]} com {ordenada[l-1]["dado"]} pontos')
print(geral)
print(jogadores)
#Solução Guanabara
'''jogo = {'jogador1:': randint(1,6),
        'jogador2:': randint(1,6),
        'jogador3:': randint(1,6),
        'jogador4:': randint(1,6),}
print(jogo)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
print('-=' * 30)
print('Ranking dos jogadores')
for i, v enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')'''
