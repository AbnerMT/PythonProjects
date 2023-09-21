num = int(input('Digite um número entre 0 e 9999: '))
unidade = num // 1 % 10 # Formula matematica para pegar a unidade
dezena = num // 10 % 10
centena = num //100 % 10
milhar = num // 1000 % 10
print(f'UNIDADE: {unidade}' )  # Unidade
print(f'DEZENA: {dezena}')  # Dezena
print(f'CENTENA: {centena} ')  # Centena
print(f'MILHAR: {milhar}')  # Milhar
# Formula Matematica''')
('''
numero = int(input('Digite um numero inteiro positivo: '))
# Extraindo a unidade
unidade = numero % 10
# Eliminando a unidade de nosso número
numero = (numero - unidade)/10
# Extraindo a dezena
dezena = numero % 10
# Eliminando a dezena do número original, fica a centena
numero = (numero - dezena)/10
centena = numero
# Fazendo ser inteiros
dezena = int(dezena)
centena = int(centena)
print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)') ''')