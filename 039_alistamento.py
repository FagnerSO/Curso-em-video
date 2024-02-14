from datetime import date
idade = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year
atual = 18 - (ano - idade)

if ano - idade == 18:
    print('É chegada a hora de se alistar, procure um centro de alistamento')
elif ano - idade < 18:
    print(f'Ainda faltam {atual} anos para voce se alistar')
else:
    print(f'Voce ja deria ter se alistado, está atrasado {abs(atual)} anos')

