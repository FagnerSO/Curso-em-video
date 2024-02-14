distancia = int(input('Digite a distancia da viagem em km: '))

if distancia <= 200:
    print(f'Sua passagem custará R${distancia * 0.50:.2f}')
else:
    print(f'Sua passagem custará R${distancia * 0.45:.2f}')