n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if media >= 7.0:
    print(f'Aluno Aprovado!! media {media:.1f} Parabens')
else:
    print(f'Aluno Reprovado!! media {media:.1f}')  # condição composta!
#  Outra forma print('Parabens' if media >= 6 else 'Estude mais')
