# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
#  utilizando um laço for.

""" Meu Programa """

n = int(input('Digite um número qualquer, será mostrado sua tabuada: '))
for c in range(1, 11):
    soma = n * c
    print('{} x {} = {}'.format(n, c, soma))

''' Do Guanabara'''

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num * c))
