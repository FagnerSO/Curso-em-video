print('#'*10, '\033[4;36;40mCalculadora de IMC\033[m', '#'*10)

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (pow(altura, 2))
ideal = imc / (pow(altura,2))

if imc < 18.5:
    print(f'Seu IMC é \033[31m{imc:.2f}\033[m, voce está abaixo do peso')
elif imc < 25:
    print(f'Seu IMC é \033[31m{imc:.2f}\033[m, voce está no seu peso ideal')
elif imc < 30:
    print(f'Seu IMC é \033[31m{imc:.2f}\033[m, voce está com sobrepeso')
elif imc < 40:
    print(f'Seu IMC é \033[31m{imc:.2f}\033[m, voce está com obesidade')
else:
    print(f'Seu IMC é \033[31m{imc:.2f}\033[m, voce está com obesidade morbida')