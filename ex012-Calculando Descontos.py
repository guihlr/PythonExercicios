# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto para calcular 5% de desconto:'))
desconto = preco-(preco*5/100)
print(f'O produto com desconto tem o preço de R${desconto:.2f}')
