nome = input('Digite o seu nome: ')  # Poderia colocar o .split aqui
print('Analisando o seu nome...')
dividir = nome.split()  # esse nome sem espaço precisa sem guardado por isso tem que ter a variável
print(f'Nome com letras Maiúsculas: ', nome.upper())  # Letras Maiusculo
print(f'Nome com letra Minúsculas: ', nome.lower())  # Letras Minusculas
print(f'Seu nome tem', len(nome.replace(' ', '')), 'Letras sem espaço')  # Conta as letras sem o espaço
print(dividir[0], 'tem', len(dividir[0]), 'Letras')  # é a primeira palavra do texto sendo contada
