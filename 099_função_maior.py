from time import sleep
def desenha_linha():
    print('-=' * 20)

desenha_linha()
def maior(*rep):
    print(f'Analisando os números passados...')
    for i in rep:
        print(i, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(rep)} valores ao todo.')
    print(f'O maior valor informado foi {max(rep)}.')
    desenha_linha()

maior(8, 9, 10, 11, 5)
maior(5,9,4)
maior(1)
maior(0)


