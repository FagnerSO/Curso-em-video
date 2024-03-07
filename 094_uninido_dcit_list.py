print(f'\033[1;33m{" Cadastro Pessoas ":=^50}\033[m')
pessoa = {}
geral = []
soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize().strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    geral.append(pessoa.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar [S/N]: ')).upper().strip()
    if resp == 'N':
        break
media = soma / len(geral)
print('-=' * 30)
print(f'O grupo tem {len(geral)} pessoas.')
print(f'A média de idade é {media:.2f}')
print(f'As mulheres cadastradas foram: ', end=' ')
for i in geral:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end=' ')
print()
print('Lista de pessoas que estão acima da média:')
for i in geral:
    if i['idade'] > media:
        print(f'Nome: {i["nome"]}, sexo: {i["sexo"]}, idade: {i["idade"]}.')
