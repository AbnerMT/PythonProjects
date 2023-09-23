n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n1  # Supondo que o meu maior número é n1
menor = n1
if n2 > maior:  # Teste! Se o n2 maior do que o n1(maior), maior = n2
    maior = n2
if n3 > maior:  # Teste! Se o n3 maior do que o maior, maior = n3
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f' O menor número é: {menor}')
print(f'O maior número é: {maior}')
