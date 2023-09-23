from time import sleep
print('-='*20)
print('Analisador de TRIÂNGULOS')
print('-='*20)
sleep(1)
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))
if a < b + c and b < a + c and c < a + b: # (a + b) > c:  or (a + c) > b or (c + b) > a:  # Formula triangulo
    print(f'È triangulo')
else:
    print(f'Não é triangulo')
