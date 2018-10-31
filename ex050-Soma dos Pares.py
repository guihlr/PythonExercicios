# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
# pares. Se o valor digitado for ímpar, desconsidere-o.

cont = 0  # Contador
soma = 0  # Acumulador
for c in range(1, 7):
    num = int(input('Digite o {}º valor : '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} valores PARES digitados é {}'.format(cont, soma))
