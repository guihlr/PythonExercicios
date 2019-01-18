# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Digite o seu nome: ')))
    temp.append(float(input('Peso: ')))
    princ.append(temp[:])
    if len(temp) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        else:
            men = temp[1]
    temp.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'nN':
        break
print('-=' * 30)
print(f'Os dados foram {princ}')
print(f'Ao todo, foram {len(princ)} pessoas cadastradas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
