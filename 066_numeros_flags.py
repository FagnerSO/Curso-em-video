print(f'{"Break com Flag":|^50}')
c = s = 0
while True:
    n = int(input('Digite um valor (999 para finalizar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Voce digitou {c} e soma total é de {s}.')