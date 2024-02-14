from random import randint

print('*****Jogo da Advinhação*****\n')
numero = int(input('Digite um número entre 0 e 10: '))
sorte = randint(0,10)
c = 0
print(sorte)
while numero != sorte:
    print('Voce errou tente novamente')
    numero = int(input('Digite um número entre 0 e 10: '))
    c += 1
print(f'Parabens voce acertou e preciou de {c} tentativas')