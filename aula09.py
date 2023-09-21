frase = 'Curso Em Video Python'
# print(frase[::2]) # A String toda quando ta com 0 o padrao e do inicio até o fim pulando 2 casas
# print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and
# scrambled it to make a type specimen book""") #Imprimir o texto completo
# print(frase.upper().count('O')) # Usando dois metodos ele analisa o texto em Maiusculo em seguida conta o nº de 'O'
# print(len(frase.strip())) #  conta os caracteres é lembrando conta até os ESPAÇOS EM BRANCO e tira os espaços

# frase = frase.replace('Python', 'Android') #Aqui ele troca efetivamente
# print('Curso' in frase)
# print(frase.find('Curso'))
dividido = frase.split()
print(dividido[2][3]) # Mostra a frase divida no caso aparece Video e pedi tbm a letra 3

