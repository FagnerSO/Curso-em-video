valor = float(input('Digite o valor do produto: R$'))
desconto = valor * 0.05
final = valor - desconto

print(f'O valor do produto com desconto de 5% será de R${final:.2f}')

salario = float(input('Digite o salario: R$'))
aumento = 0.15
total = salario * (1 + aumento)

print(f'Total salario com aumento R${total:.2f}')