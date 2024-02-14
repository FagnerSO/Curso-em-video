print(f'\033[31m{"Tratamento numeros":~^50}\033[m')
c = soma = 0

n = int(input('Digite o numero a ser somado: '))
while n != 999:
    soma = soma + n
    c += 1
    n = int(input('Digite o numero a ser somado: '))

print(f'Foram digitados um total de {c} e a soma deste núemros é {soma}')