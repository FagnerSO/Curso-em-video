print('*-'*10, '\033[1;33;107m Triangulos \033[m', '*-'*10, '\n')
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    triangulo = True
    print('\nOs segmentos podem formar um triangulo\n')
else:
    triangulo = False
    print('\nEstes segmentos não podem formar tringulo\n')

if triangulo == True and r1 == r2 and r2 == r3:
    print('Este é um triangulo\033[036m Equilátero\033[m.')
elif triangulo == True and r1 == r2 or r2 == r3 or r1 == r3:
    print('Este é um triangulo\033[036m Isóceles\033[m.')
elif triangulo == True and r1 != r2 and r2 != r3 and r3 != r1: # r1 != r2 != r3 != r4
    print('Este é um triangulo\033[036m Escaleno\033[m.')