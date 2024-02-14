from datetime import date
ano = date.today().year
menor = 0
maior = 0
e = 0

for i in range(1 , 8):
    idade = int(input(f'Em que ano a {i}ª pessoa nasceu: '))
    atual = ano - idade
    if 20 > atual > 0:
        menor += 1
    elif 20 < atual > 0:
        maior += 1
    else:
        e += 1
        print(f'Temos {e}, invalidas')
print(f'No total temos {maior} maiores de 21 anos e {menor} menores.')