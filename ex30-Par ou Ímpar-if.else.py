# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
import time
num = float(input('Digite um número: '))
print('-=-' * 10)
print('VERFICANDO NÚMERO...')
print('-=-' * 10)
time.sleep(1)
if num % 2 == 0:
    print('É Par!')
else:
    print('É Ímpar!')
