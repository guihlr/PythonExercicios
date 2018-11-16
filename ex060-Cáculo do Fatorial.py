# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# from math import factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}.'.format(n, f))

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('O fatorial de {} é {}.'.format(n, f))

n = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando o fatorial com o < for >')
f = 1
print('Calculando {}! = '.format(n), end='')
for x in range(n, 0, -1):
    print('{}'.format(x), end='')
    print(' x ' if x > 1 else ' = ', end='')
    f *= x
print('{}'.format(f))


""" Meu Programa """

n = int(input('Digite número para calular seu Fatorial: '))
f = 1
c = n
while c > 0:
    f *= c
    c -= 1
print(f'O fatorial de {n} é {f}')
