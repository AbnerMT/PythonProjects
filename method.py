n = (input('Digite algo: '))
print(type(n))
print('Só tem espaços? ', n.isspace())
print('Ele é alfabetico? ', n.isalpha())
print('Estão maiusculas ? ', n.isupper())
print('Ele é um número ? ', n.isnumeric())
print('Ele é alfanúmerico? ', n.isalnum())
print('Estão minusculas? ? ', n.islower())
print('Está capitalizada', n.istitle())