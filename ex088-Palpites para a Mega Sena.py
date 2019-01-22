# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = list()

print('=' * 40)
print(f'{"JOGUE NA MEGA SENA":^40}')
print('=' * 40)
jogador = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {jogador} JOGOS  -=-=-=')
for p in range(jogador):
    print(f'Jogo {p + 1}: ', end='')
    numeros = [randint(1, 60), randint(1, 60), randint(1, 60),
               randint(1, 60), randint(1, 60), randint(1, 60)]
    lista.append(numeros)
    print(numeros)
    sleep(1)
print('-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')
