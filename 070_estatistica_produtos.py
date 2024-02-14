print(f'\033[1;32m{" Mercadão do Guanabara ":=^50}\033[m')
total = quantidade = menor = cont = 0
nome = ''
while True:
    produto = input('Nome do produto: ').upper().strip()
    preço = float(input('Preço: '))
    total += preço
    cont += 1
    if preço > 1000:
        quantidade += 1
    if cont == 1 or preço < menor:
        menor = preço
        nome = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continua == 'N':
        break
print(f'{"FIM DO PROGRAMA":=^50}')
print(f'O total da compra foi R${total:.2f}.')
print(f'O produto mais barato foi {nome} que custa R${menor:.2f}')
print(f'Nessa lista temos {quantidade} de produtos com o valor acima de R$1.000,00')
