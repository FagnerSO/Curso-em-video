nome = input('Digite a frase: ').replace(' ','').upper()
inverso = nome[::-1]

if nome == inverso:
    print(f'O inverso de {nome} é {inverso}.\n'
          f'Temos um palindromo')
else:
    print(f'{nome}, não é um palidromo')


"""c = ''
for letra in range(len(nome) -1, -1, -1):
    c += nome[letra]
if c == nome:
    print(f'O inverso de {nome} é {inverso}.\n'
          f'Temos um palindromo')
else:
    print(f'{nome}, não é um palidromo')
"""