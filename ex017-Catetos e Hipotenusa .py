""" Faça um programa que leia o comprimento do cateto oposto de um triângulo e do cateto adjacente de um
triângulo retângulo, calcule e mostre o comprimento da hipotenusa. """

# Maneira matemática de se fazer, sem importação

# cateto_oposto = float(input('Comprimento do cateto oposto: '))
# cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}' .format(hipotenusa))

# Maneira com import math

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}' .format(hi))
