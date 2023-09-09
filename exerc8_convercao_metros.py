v = float(input('Digite o valor em [M]: '))
km = v / 1000
hm = v / 100
dam = v / 10
dm = v * 10
cent = v * 100
mili = v * 1000
print(f'O valor em [Kilometros]: {km}\n [Hectometro]: {hm}\n [Decâmetro]: {dam}\n [Decimetro]: {dm}\n [Centimetro]: {cent}\n [Milimetros]: {mili}')