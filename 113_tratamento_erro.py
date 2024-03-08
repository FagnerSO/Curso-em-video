def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('Usuario preferiu não digitar esse número')
            return 0
        else:
            return n

num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')