valor = float(input('Digite o valor do produto R$'))
print('Formas de pagamento\n'
      '[1] - à vista dinheiro / cheque\n'
      '[2] - à vista cartão\n'
      '[3] - Parcelado 2 x\n'
      '[4] - Parcelado X vezes')
pagamento = int(input('Digite a opção de pagamento: '))

if pagamento == 1:
    print(f'O valor da sua compra é \033[31mR${valor:.2f}\033[m, a vista em dinheiro '
    f'com desconto de 10% , o valor para pagamento será de \033[31mR${valor - (valor * 0.10):.2f}\033[m')
elif pagamento == 2:
    print(f'O valor da sua compra é \033[31mR${valor:.2f}\033[m, a vista com cartão '
          f'com desconto de 5% , o valor para pagamento será de \033[31mR${valor - (valor * 0.05):.2f}\033[m')
elif pagamento == 3:
    print(f'O valor da sua compra é \033[31mR${valor:.2f}\033[m, parcelado em \033[31m2x\033[m '
        f'sem acréscimo, o valor da parcela será de \033[31mR${valor / 2:.2f}\033[m')
elif pagamento == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    print(f'O valor da sua compra é \033[31mR${valor:.2f}\033[m, parcelado em \033[31m{parcelas}x\033[m '
        f'com acréscimo de 20%, o valor da parcela será de \033[31mR${(valor * 1.20) / parcelas:.2f}\033[m')