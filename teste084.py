# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    princ.append(temp[:])
    maior = max(princ)[1]
    menor = min(princ)[1]
    temp.clear()

    resp = str(input('Continuar? [S/N] '))
    if resp in 'nN':
        break

print(f'Ao todo, foram {len(princ)} pessoas cadastradas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
