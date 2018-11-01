# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

""" Meu Programa """

from datetime import date

atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Ano de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} Pessoas atingiram a maioridade'.format(maior))
print('{} Pessoas ainda não atingiram a maioridade'.format(menor))

''' Do Guanabara '''

atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todos tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
