# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import emoji
from time import sleep

print('-=-' * 15)
print('SE PREPARE !!!')
print('CONTAGEM REGRESSIVA PARA A QUEIMA DE FOGOS!')
print('-=-' * 15)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('BOOM! :fireworks: '), end='')
print(emoji.emojize('BOOM! :fireworks: '), end='')
print(emoji.emojize('POOOW! :fireworks:'))
print('FELIZ ANO NOVO!')