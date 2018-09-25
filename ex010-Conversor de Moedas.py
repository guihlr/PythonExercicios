# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
print('Converter seu dinheiro de real para dólar!')
print()
cart = float(input('Digite quanto dinheiro em R$, voce tem:'))
rs = 3.27
dl = 1.00
gt = cart/rs*dl
print('Você pode comprar {:.2f} dólares!' .format(gt))
