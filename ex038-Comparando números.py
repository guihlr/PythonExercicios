# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

""" Meu Programa """

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print('O primeiro valor é maior')
if n1 < n2:
    print('O segundo valor é maior')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')

''' Do Guanabara '''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é o maior')
elif n2 > n1:
    print('O SEGUNDO valor é o maior')
else:
    print('Os dois valores são IGUAIS')