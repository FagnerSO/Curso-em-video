from time import sleep


def desenha_linha():
    print('-=' * 20)


def contador(i, f, p):
    p = abs(p)
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for j in range(i, f, p):
            print(j, end=' ')
            sleep(0.1)
        print('FIM!')
    elif i > f:
        for j in reversed(range(f, i, p)):
            print(j, end=' ')
            sleep(0.1)
        print('FIM!')
    desenha_linha()


contador(1, 10, 1)
contador(50, 2, 5)

print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

#Solução Guanabara

'''def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    desenha_linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
desenha_linha()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)'''

