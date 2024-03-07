time = []
jogador = {}
gols = []
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome: ')).capitalize()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for k in range(jogador['partidas']):
        gols.append(int(input(f'Quantos gols marcados na partida {k + 1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja Continuar [S/N]: ')).upper().strip()
        if resp in 'SN':
            print('-' * 30)
            break
        print('Opção Invalida! Digite S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)
while True:
    cod = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if cod == 999:
        print('Volte Sempre!!')
        break
    if cod >= len(time):
        print('Erro este jogador não esta na lista.')
    else:
        print(f'O jogador \033[7m{time[cod]["nome"].upper()}\033[m jogou {time[cod]["partidas"]} partidas.')
        for k, v in enumerate(time[cod]['gols']):
            print(f'=> Na partida {k + 1} ele fez {v} gols.')
        print(f'Fez um total de {time[cod]["total"]} de gols.')
