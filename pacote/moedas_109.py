def metade(n, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumento(n, a, formato=False):
    res = n + (n * (a / 100))
    return res if formato is False else moeda(res)


def reducao(n, r, formato=False):
    res = n - (n * (r / 100))
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')