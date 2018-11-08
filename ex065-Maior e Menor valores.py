# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se
# ele quer ou não continuar a digitar valores.

""" Fazer esse sozinho nas férias e estudar """

resp = 'S'
# media = soma = qtd = maior = menor = 0  # pode ser feito assim
media = 0
soma = 0
qtd = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        # maior = menor = num  # pode ser feito assim
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / qtd
print('Você digitou {} números e a média foi {}.'.format(qtd, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
