import math

angulo = float(input('Digite um angulo: '))
rad = math.radians(angulo)
sen = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)

print(f'Convertendo o angulo digitado de {angulo:.0f}° para radianos o valor encontrado é {rad},\n'
      f'seno = {sen:.2f}\n'
      f'cosseno = {cos:.2f}\n'
      f'tangente = {tang:.2f}')