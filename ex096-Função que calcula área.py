# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def área(l, c):
  soma = l * c
  print(f"A área de um terreno de {l}x{c} é de {soma}m²")

# Programa Principal
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
área(l, c)
