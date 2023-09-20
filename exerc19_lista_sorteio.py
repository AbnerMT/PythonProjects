from random import choice
nome1 = input('Escreva o nome do primeiro aluno: ')
nome2 = input('Escreva o nome do segundo aluno: ')
nome3 = input('Escreva o nome do terceiro aluno: ')
nome4 = input('Escreva o nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print(f'A aluno sorteado é: ', escolhido )

