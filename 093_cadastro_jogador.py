jogador = {'nome': input('Nome: ').capitalize()}
gols = []
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for i in range(partidas):
    gols.append(int(input(f'Quantos gols marcados na partida {i+1}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, j in enumerate(jogador['gols']):
    print(f'=> Na partida {i+1} ele fez {j} gols.')
print(f'Fez um total de {jogador["total"]} de gols.')
