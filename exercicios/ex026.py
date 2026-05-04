nome = input('Escreva seu nome completo: ').strip()
print(f'Seu nome em maiusculas: {nome.upper()}')
print(f'Seu nome em minusculas: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(' ')} letras')
val = nome.split()
print(f'Seu primeiro nome é {val[0]} e tem {len(nome.split())}')


