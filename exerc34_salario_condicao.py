salario = float(input('Digite o seu salário: '))
if salario <= 1250:
    aumento = (salario * 15) / 100  # primeiro aumento apenas 15%
    print(f'O seu salario era de {salario} e o seu novo salário é {salario+aumento:.2f}')
else:
    aumento2 = (salario * 10) / 100  # segundo aumento apenas 10%
    print(f'O seu salário era {salario} e o seu novo salário é {salario+aumento2:.2f}')
