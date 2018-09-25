# Crie um programa que leia um número Real qualquer pelo teclado e mostre a sua porção Inteira.
# Ex: Digite um número: 6.127 => O número 6.127 tem a parte Inteira 6.

from math import trunc

n = float(input('Digite um número Real qualquer, para eu converte-lo para um número Inteiro: '))
i = trunc(n)
print('O número {} tem a parte Inteira de {}.' .format(n, i))
