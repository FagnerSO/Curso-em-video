print(f'\033[31m{" Lista Ordenada ":=^50}\033[m')

lista = []

while len(lista) != 5:
    numero = int(input('Digite um valor inteiro: '))
    if numero not in lista:
        posicao = 0
        while posicao < len(lista) and numero > lista[posicao]:
            posicao += 1
        lista.insert(posicao, numero)
        print(f'Adicionado na posição {posicao} da lista.')
    else:
        print('Valor duplicado! Digitar novamente...')
print('-=' * 30)
print(f'Os valores digitador em ordem foram {lista}')

#Solução Guanabara

'''lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c ==0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitador em ordem foram {lista}')'''