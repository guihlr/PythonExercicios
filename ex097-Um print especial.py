# Faça um programa que tenha uma função chmada escreva(), que receba um texto qualquer
# como parâmetro e mostra uma mensagem com tamanho adaptável.

def escreva(msg):
  print('~' * len(msg))
  print(msg)
  print('~' * len(msg))
  # var = '~'
  # for p in msg:
  #   var += '~'
  # print(var)
  # print(msg)
  # print(var)


#Programa Principal
escreva('Guilherme Henrique')
escreva('Curso de Python no Youtoba')
escreva('CeV')