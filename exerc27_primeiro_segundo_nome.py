nomecompleto = str(input('Digite o seu nome completo: ')).strip()
print('Muito prazer em te conhecer')
separar = nomecompleto.split()
print('[PRIMEIRO NOME]:', separar[0]) # Separei apenas o 1 indíce
print('[SEGUNDO NOME]:', separar[-1]) # Separei apenas o segundo indíce
