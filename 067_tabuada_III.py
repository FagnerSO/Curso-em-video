print(f'{"Taboada com break":=^50}')
while True:

    n = int(input('Digite um numero: '))
    print('-'*50)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('-' * 50)
print('Programa tabuada encerrado!!')