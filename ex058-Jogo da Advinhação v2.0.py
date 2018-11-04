# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que
#  agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

""" Meu Programa """

from random import randint

computador = randint(0, 10)
palpite = int(input('''
Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?
Qual é o seu palpite? '''))
cont = 1  # inicializando o contador.
while palpite != computador:
    cont += 1  # contador, ira contar quantas vezes o laço foi repetido.
    if palpite < computador:
        palpite = int(input('Mais... Tente mais uma vez. '))
    if palpite > computador:
        palpite = int(input('Menos... Tente mais uma vez. '))
print('O computador pensou no número {}, e você acertou com {} tentativas. Parabéns!'.format(computador, cont))

""" Do Guanabara """

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... Tente novamente. ')
        elif jogador > computador:
            print('Menos ... Tente novamente.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))