sexo = input('Digite o sexo [M / F]: ').upper()

while (sexo != 'F') and (sexo != 'M'):
    print('Voce digitou um valor invalida, digite novamente')
    sexo = input('Digite o sexo [M / F]: ').upper()
print('Informação arquivada com sucesso')