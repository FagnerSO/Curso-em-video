numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete', 'oito',
'nove', 'dez', 'onze','doze', 'treze', 'catorze', 'quinze', 'dezesseis','dezessete',
'dezoito', 'dezenove', 'vinte')

while True:
    pesquisa = int(input('Digite um número entre 0 e 20: '))
    if 0 <= pesquisa <= 20:
        break
    print('Tente novamente. ', end='')

print(f'Voce digitou o numero {numeros_por_extenso[pesquisa]}.')
