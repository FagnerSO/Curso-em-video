print(f'\033[1;33;7m{" LISTAGEM PREÇOS ":=^40}\033[m')
itens_escolares = ('Lápis', 1.50, 'Caneta esferográfica', 2.00, 'Caderno', 10.50, 'Borracha', 1.00, 'Estojo', 5.50,
                   'Régua', 1.75, 'Cola', 2.50, 'Tesoura', 3.00, 'Mochila', 20.00, 'Apontador', 1.25,
                   'Lápis de cor (12 cores)', 8.75, 'Bolsa térmica para lanche', 12.00, 'Pasta organizadora', 4.50,
                   'Agenda escolar', 7.00, 'Giz de cera (24 cores)', 6.50)

for pos in range(0, len(itens_escolares), 2):
    print(f'{itens_escolares[pos]:.<30}R${itens_escolares[pos + 1]:>7.2f}')