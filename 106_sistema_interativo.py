def frase(txt, corl=0, corf=0):
    """

    :param txt:
    :param corl:
    :param corf:
    :return:
    """
    print(f'\033[1:{corl}:{corf}m{"":~^{len(txt) + 2}}')
    print(f'{txt:^{len(txt) + 2}}')
    print(f'{"":~^{len(txt) + 2}}')
    print(end='\033[m')
def ajuda(msg):
    """

    :param msg:
    :return:
    """
    while True:
        frase('SISTEMA DE AJUDA PyHELP', 97, 42)
        n = str(input(msg)).lower()
        if n == 'fim':
            frase('ATÉ LOGO', 97, 41)
            break
        else:
            frase(f'Acessando o manual do comando {n}', 97, 44)
            print(end='\033[1:30:107m')
            help(n)



ajuda('Função ou Biblioteca > ')
