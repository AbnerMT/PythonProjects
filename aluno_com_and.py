q_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if q_faltas <= 5 and media_final >= 7: #AND tem que atender as duas condições! senao da errado!
    print('Aluno Aprovado')
else:
    print('Aluno REPROVADO')