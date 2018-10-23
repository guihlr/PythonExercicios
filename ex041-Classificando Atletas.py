# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

""" Meu Programa """

from datetime import date

nasci = int(input('Ano de nascimento: '))
ano = date.today().year
ano_nasci = ano - nasci
if ano_nasci <= 9:
    print('Você tem {} anos, e sua categoria é MIRIM'.format(ano_nasci))
elif ano_nasci <= 14:
    print('Você tem {} anos, e sua categoria é INFANTIL'.format(ano_nasci))
elif ano_nasci <= 19:
    print('Você tem {} anos, e sua categoria é JÚNIOR'.format(ano_nasci))
elif ano_nasci <= 25:
    print('Você tem {} anos, e sua categoria é SÊNIOR'.format(ano_nasci))
else:
    print('Você tem {} anos, e sua categoria é MASTER'.format(ano_nasci))

''' Do Guanabara'''

atual = date.today().year
nascimento = int(input('Ano Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
