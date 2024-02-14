print(f'\033[31m{"MAIOR - MENOR":~^50}\033[m')
numeros = []
continua = 'S'
while continua != 'N':
    numeros.append(int(input('Digite um numero: ')))
    continua = input('Deseja continuar [S / N]: ').upper().strip()
print(f'Voce digitou {len(numeros)} números, a media foi {sum(numeros) / len(numeros)}')
print(f'O maior valor foi {max(numeros)} e o menor valor foi {min(numeros)}')
print(numeros[1])
#Solução Guanabara
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0] #somente 1ª letra
media = soma / quant
print(f'Voce digitou {quant} números, a media foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')