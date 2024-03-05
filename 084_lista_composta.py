print(f'\033[30:42m{"Lista Composta ":=^50}\033[m')
lista = []
pessoas = []
pesado = []
leve = []
maior = menor = 0
while True:
    lista.append(str(input('Digite o nome da pessoa: ')))
    lista.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar [S/N]: ').upper().strip()[0]
        if resp not in 'SN':
            print('Opção invalida.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso encontrado foi de {maior}kg. Peso de', end=' ')
for pes in pessoas:
    if pes[1] == maior:
        print(pes[0], end=' ')
print(f'\nO menor peso encontrado foi de {menor}kg. Peso de', end=' ')
for pes in pessoas:
    if pes[1] == menor:
        print(pes[0], end=' ')
