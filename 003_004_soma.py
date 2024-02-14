n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2

print(f'A soma de {n1} e {n2} é {s}')

n3 = input('Digite algo: ')

print(n3.isnumeric())
print(n3.isalnum())
print(n3.isspace())
print(type(n3))