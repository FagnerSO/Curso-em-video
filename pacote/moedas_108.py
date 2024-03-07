def metade(n):
    n = n / 2
    return n


def dobro(n):
    n = n * 2
    return n


def aumento(n, a):
    n = n + (n * (a / 100))
    return n


def reducao(n, r):
    n = n - (n * (r / 100))
    return n


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco}'.replace('.', ',')