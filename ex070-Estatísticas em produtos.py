# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

"""" Fazer sozinho e estudar nas férias! """

total = mais1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    total += preco
    if preco > 1000:
        mais1000 += 1
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto na compra é de R${total:.2f}')
print(f'{mais1000} produtos custam mais de R$1.000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

