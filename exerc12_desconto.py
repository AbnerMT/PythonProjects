preco = float(input('Digite o valor do produto R$: '))
descont = (preco * 5)/100 # Achei o desconto
des = preco - descont #Subtrair o desconto - preço

print(f'O valor do desconto é R${round(descont, 2)} é o valor do produto com [DESCONTO] é: R${round(des, 2)}')