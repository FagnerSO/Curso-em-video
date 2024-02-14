n1 = float(input('Digite a primiero nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print(f'Voce esta aprovado sua media foi {media:.2f}')
elif media < 5:
    print(f'Voce está reprovado sua media foi {media:.2f}')
else:
    print(f'Voce esta de recuperação sua media foi {media:.2f}')