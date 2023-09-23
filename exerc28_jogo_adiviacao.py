from random import randint  # importei apenas o modulo que vou utilizar!
from time import sleep
numero = randint(0, 5)  # sorteando número inteiro
numcerto = int(input('Digite um número: '))
print('PROCESSANDO')
sleep(2)  # Faz com que o pc 'espere' por 2 segundos
print('-=-' * 12)
print('Pesando em um número entre 0 e 5...')
print('-=-' * 12)
if numero == numcerto:
    print(f'Você acertou o número {numero}!!Parabéns.')
else:
    print(f'Você errou eu pensei no número {numero}!!Que pena.')
