peso = []

for i in range(1, 4):
    peso.append(float(input(f'Digite o peso da {i} pessoa: ')))
print(f'O maior peso digitado foi {max(peso)}')
print(f'O maior peso digitado foi {min(peso)}')