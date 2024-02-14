velocidade = int(input('Digite a velocodade registrada em km/h: '))
limite = 80

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print(f'Voce foi multado, ultrapassou a velocidade em {velocidade - limite}km/h e o valor da multa será de R${multa:.2f}')
else:
    print('Boa Viagem')