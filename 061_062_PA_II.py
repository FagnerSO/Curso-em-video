print('{:=^50}'.format('CALCULADORA DE PA'))

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
termo = int(input('Digite quantos termos tera sua PA: '))
c = 0
total = 0

while termo != 0:
    total = total + termo
    while c < total:
        print(primeiro_termo, end='-')
        primeiro_termo += razao
        c += 1
    print('PAUSA')
    termo = int(input('Quantos termos mostrar: '))
print(f'Progerssão finalizada com {total} mostrados.')
