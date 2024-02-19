print(f'\033[1;32;7m{" :/ ":=^50}\033[m')
valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    for i in range(len(valor)):
        for j in range(i + 1, len(valor)):
            if valor[i] == valor[j]:
                print('Valor duplicado, não adicionado')
                valor.pop()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]: ')).upper().replace(' ', '')[0]
    if continua == 'N':
        break

print(valor)
valor.sort()
print(valor)

# SOLUÇÃO GUANABARA

'''numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:  # esta linha substitui da 4 a 9
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')'''
