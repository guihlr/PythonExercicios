# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()
for l in range(0, 5):
    lista.append(int(input(f'Digite um valor a posição {l}: ')))
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitador foi {max(lista)} nas posições ', end='')
for pos in range(0, 5):
    if lista[pos] == max(lista):
        print(f'{pos}...', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for pos in range(0, 5):
    if lista[pos] == min(lista):
        print(f'{pos}...', end='')
