# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrado.
# C) quantas mulheres tem menos de 20 anos.

""" Fazer sozinho e estudar nas férias"""

tot18 = totH = totM20 = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    nome = str(input('Nome: ')).strip()  # fiz a mais
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F':
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        print('-' * 30)
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrado.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
