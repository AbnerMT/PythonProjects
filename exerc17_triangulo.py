from math import hypot
catetooposto = float(input('Digite o cateto oposto: ')) #lado
catetoadjacente = float(input('Digite o cateto adjacente: ')) # base
hipotenusa = hypot(catetooposto, catetoadjacente)
print(f'O calculo da hipotenusa é : {hipotenusa:.2f}') # Atenção! são dois valores