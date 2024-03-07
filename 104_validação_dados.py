'''def leiaInt(num=input('Digite um número: ')):
    while True:
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[31mERRO! Digite um número valido inteiro\033[m')
            num = input('Digite um número: ')
    return num


n = leiaInt()
print(f'Voce acabou de digitar o numero {n}')
'''
#Solução Guanabara

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número valido inteiro\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Voce digitou o número {n}.')