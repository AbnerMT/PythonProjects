km = int(input('Velocidade: '))
if km > 80:
    multiplicar = (km - 80) * 7  # formula
    print(f'Você foi multado! a sua multa é de R$ {multiplicar:.2f}')  # A cada km é R$ de multa
print('Tenha um bom dia! Diriga com segurança.') #condição simples
