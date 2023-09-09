dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos [KM] rodados? '))
pdia = (dia * 60) + (km * 0.15)
print(f'Foram {dia}[DIAS] cerca de {km}[KM] rodados é o total é R${pdia:.2f}')
