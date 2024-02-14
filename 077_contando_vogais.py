print(f'\033[1;33;7m{" BUSCANDO VOGAIS ":=^50}\033[m')

palavras_tupla = ('banana', 'computador', 'livro', 'carro', 'cachorro', 'chocolate',
            'telefone', 'guitarra', 'sol', 'caneta')

for palavra in palavras_tupla:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')