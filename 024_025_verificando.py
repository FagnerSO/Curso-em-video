nome = input('Digite o nome da cidade: ').strip().title()
primeiro = nome.split()
conf_1 = (primeiro[0] == 'Santo')
conf_2 = (nome.find('Silva') != -1) == True

print(f'Nome digitado: {nome}\n'
      f'Começa com Santo: {conf_1}\n')

print(f'Tem Silva no nome: {conf_2}\n')

# Forma mais simples de localizar utilizando fatiamento
print(nome[:5] == 'Santo')

print('Silva' in nome)