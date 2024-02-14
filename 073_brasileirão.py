times_serie_a_2021_colocacao = ('Palmeiras', 'Atlético Mineiro', 'Flamengo', 'Grêmio', 'Fluminense',
    'Internacional', 'São Paulo', 'Athletico Paranaense', 'Ceará', 'Fortaleza',
    'Santos', 'Atlético Goianiense', 'Corinthians', 'Bahia', 'Juventude', 'Sport Recife',
    'Cuiabá', 'América Mineiro', 'Chapecoense', 'Goiás')
print(f'\033[1;32;7m{" CLASIFICADOS LIBERTADORES ":=^50}\033[m')
for posição in range(0, 5):
    print(f'{posição + 1}º colocado {times_serie_a_2021_colocacao[posição]}')

print(f'\033[1;32;7m{" REBAIXADOS ":=^50}\033[m')
for pos, time in enumerate(times_serie_a_2021_colocacao[-4:]):
    print(f'{times_serie_a_2021_colocacao.index(time) + 1}º colocado {time}')

print(f'\033[1;32;7m{" CADE A CHAPECOENSE ":=^50}\033[m')
for chap in times_serie_a_2021_colocacao:
    if chap == 'Chapecoense':
        print(f' A {chap} está em {times_serie_a_2021_colocacao.index(chap) + 1}º lugar.')

print(f'\033[1;32;7m{" TIMES EM ORDEM ALFABETICA ":=^50}\033[m')
for alfa in sorted(times_serie_a_2021_colocacao):
    print(f'{alfa}', end=' - ')

