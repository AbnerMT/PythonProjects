frase = input('Digite uma frase: ').strip().upper() # Tirei os espaços e coloquei os A e a
print(frase.count('A'), 'Letras A')  # Faz a contagem da letra 'A'
print('Primeira Posição ', frase.find('A') + 1)  # Delimitei a contagem apenas para a primeira string entre 0 é 1
print('Ùltima Posição',frase.rfind('A') + 1)  # Delimitei a contagem apenas para procurar ao lado Direito iniciando no 0 só que n sei o final por isso está vazio