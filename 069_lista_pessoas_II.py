print(f'\033[1:32m{"Análise de dados":=^50}\033[m')
ida = homem = mulher = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().replace(' ', '')[0]
    if idade > 18:
        ida += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    print('~' * 30)
    continua = str(input('Deseja continuar [S/N]: ')).upper().replace(' ', '')
    print('~' * 30)
    if continua == 'N':
        break
print(f'Nesse grupo temos {homem} homens\n'
      f'Um total de {ida} pessoas com mais de 18 anos\n'
      f'E {mulher} mulheres com menos de 18 anos')