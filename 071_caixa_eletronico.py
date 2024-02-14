print(f'\033[1;32;7m{" Banco Python ":=^50}\033[m')
saque = int(input('Qual o valor que deseja sacar? R$'))

c50 = saque // 50
c2 = saque % 50
c20 = c2 // 20
c4 = c2 % 20
c10 = c4 // 10
c6 = c4 % 10
c1 = c6 // 1
c8 = c6 % 1

if c50 != 0:
    print(f'Total de {c50} cédulas de R$50,00')
if c20 != 0:
    print(f'Total de {c20} cédulas de R$20,00')
if c10 != 0:
    print(f'Total de {c10} cédulas de R$10,00')
if c1 != 0:
    print((f'Total de {c1} cédulas de R$1,00'))



#Solução Guanabara

#ir tirando cedula a cedula