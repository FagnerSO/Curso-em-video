print('*****MENU_OPÇÕES*****\n')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = 0

while menu != 5:
    print('[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior\n'
          '[4] novos numeros\n'
          '[5] sair do programa')
    menu = int(input('Digite a opção desejada: '))
    if menu == 1:
        print(f'\n\033[7mA soma dos números {n1} + {n2} = {n1 + n2}\033[m\n')
    elif menu == 2:
        print(f'\n\033[7mA multiplicação de {n1} x {n2} = {n1 * n2}\033[m\n')
    elif menu == 3:
        if n1 > n2:
            print('\n\033[7mO primeiro numero digitado é maior\033[m\n')
        else:
            print('\n\033[7mO segundo número digitado é maior\033[m\n')
    elif menu == 4:
        print('\n')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('\n')
print('\nPrograma Finalizado!!!')