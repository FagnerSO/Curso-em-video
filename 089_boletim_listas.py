geral = []
nome = []
notas = []

while True:
    nome.clear()
    notas.clear()
    nome.append(str(input('Digite o Nome do Aluno: ')))
    notas.append(float(input('Digite a nota: ')))
    notas.append(float(input('Digite a nota: ')))
    media = (notas[0] + notas[1]) / 2
    nome.append(notas[:])
    nome.append(media)
    geral.append(nome[:])
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar [S/N]: ').upper().strip()[0]
        if resp not in 'SN':
            print('Opção invalida.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"N°":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-' * 30)
for pos, g in enumerate(geral):
    print(f'{pos:<4} {g[0]:<10} {g[2]:>8.1f}')
print('-' * 30)

while True:
    n = int(input('Mostrar as notas de qual aluno [999 interrompe]: '))
    if n == 999:
        print('Finalizando...')
        break
    if n <= len(geral) - 1:
        print(f'As notas de {geral[n][0]} são {geral[n][1]}')
print('<<<Volte sempre>>>')

#Solução Guanabara

'''ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    '''