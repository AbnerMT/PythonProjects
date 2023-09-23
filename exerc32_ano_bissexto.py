from datetime import date
ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year  # Vai pegar a data de hoje, mas apenas o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano {ano} é bissexto!')
else:
    print(f'Ano {ano} Não é bissexto!')
