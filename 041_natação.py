from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print(f'Sua idade atual é \033[036m{idade} anos\033[m, voce esta no time \033[036m mirim\033[m')
elif idade <= 14:
    print(f'Sua idade atual é \033[036m{idade} anos\033[m, voce esta no time \033[036m infantil\033[m')
elif idade <= 19:
    print(f'Sua idade atual é \033[036m{idade} anos\033[m, voce esta no time \033[036m junior\033[m')
elif idade == 20:
    print(f'Sua idade atual é \033[036m{idade} anos\033[m, voce esta no time \033[036m senior\033[m')
else:
    print(f'Sua idade atual é \033[036m{idade} anos\033[m, voce esta no time \033[036m master\033[m')