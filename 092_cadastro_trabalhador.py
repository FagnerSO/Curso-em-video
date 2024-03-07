from datetime import date

trabalhador = {'nome': input('Nome: ').capitalize(),
               'idade': date.today().year - int(input('Ano de Nascimento: ')),
               }
ctps =  int(input('Carteira de Trabalho [0 não tem]: '))
if ctps > 0:
    trabalhador['ctps'] = ctps
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + (trabalhador['contratação'] + 35) - date.today().year
print('-=' * 30)
for i, j in trabalhador.items():
    print(f'{i} tem o valor de {j}')
