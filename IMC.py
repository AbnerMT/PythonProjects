print('===========================')
print('            IMC            ')
print('===========================')
peso = float(input('Digite o seu peso[Kg]: ')) #A string vai ser convertida para o tipo Real
altura = float(input('Digite a sua altura[M]: '))

imc = peso/(altura * altura) #Formula do IMC
print(f'Seu IMC = {round(imc, 1)}')
if imc < 18.5: # CLASSIFICAÇÃO de Indíce de Massa Corporal
    print("Abaixo do normal!")
elif imc <= 24.9:
    print("Normal!")
elif imc <= 29.9:
    print("Sobrepeso!")
elif imc <= 34.9:
    print("Obesidade grau I!")
elif imc <= 39.9:
    print("Obesidade grau II!")
else:
    print("Obesidade grau III, Procure um ESPECIALISTA!")
