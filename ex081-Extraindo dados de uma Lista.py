# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    lista.sort(reverse=True)

    r = str(input('Deseja continuar? [S/N]'))
    if r in 'nN':
        break
print('-=' * 30)
print(f'Foram digitados {len(lista)} elementos.')
print(f'A lista ordenada de forma decrescente: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
