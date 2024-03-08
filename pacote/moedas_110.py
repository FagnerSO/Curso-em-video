def metade(preco, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def dobro(preco, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def aumento(preco, taxaa, formato=False):
    res = preco + (preco * (taxaa / 100))
    return res if formato is False else moeda(res)


def reducao(preco, taxar, formato=False):
    res = preco - (preco * (taxar / 100))
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'O dobro do preço \t{dobro(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumento(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{reducao(preco, taxar, True)}')
    print('-' * 30)
