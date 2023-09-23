distancia = int(input('Qual é a distância em [KM]: '))
preco1 = distancia * 0.50
preco2 = distancia * 0.45
if distancia <= 200:  # Condição composta! Se estiver colado na esquerda vai acontecer sempre
    print(f'O valor será de R${preco1:.2f}')  # se for menor do que 200 vai pagar 0.50 por km
else:
    print(f'O valor será de R${preco2:.2f}')  # se for maior do que 200 vai pagar 0.45 por km
# Outra maneira: preco = distancia * 0.50 if distancia <= 200 else distancia *0.45