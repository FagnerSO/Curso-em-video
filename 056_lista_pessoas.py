print('*'*10, 'Comparação de nome, idade e sexo', '*'*10, '\n')
soma = 0
c = 0
homem = []
homem_idade = []
m = 0
for i in range(1, 5):
    print('-'*5, f'{i}ª PESSOA', '-'*5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    soma += idade
    c += 1
    if sexo == 'F' and idade < 20:
        m +=1
    elif sexo == 'M':
        homem.append(nome)
        homem_idade.append(idade)
h = (homem_idade.index(max(homem_idade)))
media = soma / c
print(f'\nA média de idade do grupo é \033[7m{media}\033[m anos\n')
print(f'Nesse grupo há \033[7m{m}\033[m mulheres com menos de 20 anos\n')
print(f'O homem mais velho do grupo é \033[7m{homem[h]}\033[m, com \033[7m{max(homem_idade)}\033[m anos')

#Solução GUANABARA para parte homem
'''maioridadehomem = 0
nomevelho = ''

for i in range(1, 5):
    print('-'*5, f'{i}ª PESSOA', '-'*5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    soma += idade
    if i == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome'''