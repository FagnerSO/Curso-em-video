print('#'*10, '\033[1;31mPrograma Minha Casa Minha Vida\033[m', '#'*10)

imovel = float(input('Digite o valor do imóvel R$'))
salario = float(input('Digite sua renda mensal R$'))
anos = int(input('Digite em quantos anos pretende financiar: '))
meses = anos * 12
prest = imovel / meses

if prest < salario * 0.30:
    print(f'Parabens!!! Seu financiamento foi aprovado, em \033[32m{meses}\033[m parcelas de \033[32mR${prest:.2f}\033[m')
else:
    print(f'Seu financimento foi negado, para aprovação a parcela deve ser inferior a \033[31mR${salario * 0.30:.2f}')