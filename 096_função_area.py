print(f'\033[31m{"Calculadora de area":*^50}\033[m')


def area_quadrada(l, c):
    area = l * c
    print(f'A área do terreno de {l}m x {c}m é de {area:.2f}m²')


larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area_quadrada(larg, comp)
