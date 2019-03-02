# Faça um programa que tenha uma função chmada escreva(), que receba um texto qualquer
# como parâmetro e mostra uma mensagem com tamanho adaptável.

def escreva(msg):
  print(len(msg) * "~")
  print(msg)
  print(len(msg) * "~")
  """var = "~"
  for p in msg:
    var += "~"
  print(var)
  print(msg)
  print(var)"""

# Programa Principal
escreva("Texto")
escreva("Meu nome é: Guilherme Henrique")
escreva("Exercício de Fixação!")