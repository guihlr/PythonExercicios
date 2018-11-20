# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

""" Meu Programa """

import random

tot = 0
while True:
    player = int(input('Diga um valor: '))
    p = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    cpu = random.randint(0, 10)
    soma = player + cpu
    if soma % 2 == 0 and p in 'Pp':
        tot += 1
        print(f'Você jogou {player} e o computador {cpu}. Total de {soma} DEU PAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    elif soma % 2 == 1 and p in 'Ii':
        tot += 1
        print(f'Você jogou {player} e o computador {cpu}. Total de {soma} DEU ÍMPAR')
        print('Você VENCEU!')
        print('''Vamos jogar novamente...''')
    else:
        if soma % 2 == 0:
            msg = 'PAR'
        else:
            msg = 'ÍMPAR'
        print(f'Você jogou {player} e o computador {cpu}. Total de {soma} DEU {msg} ')
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {tot} vezes.')
        break

""" Do Guanabara """

from random import randint

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Você Perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
