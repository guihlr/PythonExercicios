# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quanparada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).do o usuário
# digitar o valor 999, que é a condição de

soma = cont = 0
while True:
    n = int(input('Digite um valor: [999 para PARAR] '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}')
