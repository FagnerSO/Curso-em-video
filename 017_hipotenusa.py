import math
from math import sqrt, hypot

c_oposto = float(input('Digite o cateto oposto: '))
c_adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa_1 = sqrt((pow(c_oposto, 2) + pow(c_adjacente, 2)))
hipotenusa_2 = math.hypot(c_oposto, c_adjacente)
hipotenusa_3 = (c_adjacente**2 + c_oposto**2) ** 0.5

print(f'A hipotenusa 1 é {hipotenusa_1:.2f}')

print(f'A hipotenusa 2 é {hipotenusa_2:.2f}')

print(f'A hipotenusa 3 é {hipotenusa_3:.2f}')

