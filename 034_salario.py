salario = float(input('Digite o salario R$'))

if salario > 1250:
    print(f'Seu aumento será de 10%, seu novo salario será de R${salario * 1.1:.2f}')
else:
    print(f'Seu aumento será de 15%, seu novo salario será de R${salario * 1.15:.2f}')