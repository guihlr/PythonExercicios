# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se
# ele quer ou não continuar a digitar valores.

resp = 'S'
media = soma = qtd = maior = menor = 0
while resp in 'Ss':  # enquanto minha resposta estiver em 'Ss'
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
media = soma / qtd
print(f'Você digitou {qtd} números e a média foi {media}')
print(f'o maior valor foi {maior} e o menor foi {menor}')
