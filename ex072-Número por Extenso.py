# Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

""" Meus Programas """
"""n = int(input('Digite um número entre 0 e 20: '))
while n > 20 or n < 0:
    print('Tente novamente. ', end='')
    n = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {cont[n]}')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Tente novamente. ', end='')
    else:
        print(f'Você digitou o número {cont[n]}')
        break"""

""" Do Guanabara """
"""while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
    print(f'Você digitou o número {cont[num]}')"""

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[n]}')
for p in cont:
    p = input('Deseja continuar? [S/N] ')
    if p.upper() == 'S':
        n = int(input('Digite outro número entre 0 e 20: '))
        print(f'Você digitou o número {cont[n]}')
    else:
        break

