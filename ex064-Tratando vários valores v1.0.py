# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
# a soma entre eles (desconsiderando o flag).

""" Fazer esse sozinho nas férias e estudar """

'''num = cont = soma = 0 # pode ser feito assim
num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma += num
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, soma - 999))'''

# melhor forma de se fazer
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
