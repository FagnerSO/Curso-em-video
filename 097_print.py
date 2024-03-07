def frase(txt):
    print(f'{"":*^{len(txt) + 2}}')
    print(f'{txt:^{len(txt) + 3}}')
    print(f'{"":*^{len(txt) + 2}}')
    print()


frase('Ola, Mundo!')
frase('Curso em Video')
frase('O rato roeu a roupa do rei de roma')
