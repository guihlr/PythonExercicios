# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# from random import randint
# num_aleatorio = randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)
# print(num_aleatorio)
# print(f'o menor valor foi {min(num_aleatorio)}')
# print(f'o maior valor foi {max(num_aleatorio)}')

from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100),
           randint(1, 100), randint(1, 100),)
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
