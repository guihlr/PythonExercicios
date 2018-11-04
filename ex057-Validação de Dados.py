# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

""" Meu Programa

sexo = str(input('Informe seu sexo: [M/F] ')).upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
if sexo == 'F' or sexo == 'M':
    print('Sexo {} registrado com sucesso.'.format(sexo)) """

""" Outra lógica 

s = str(input('Informe seu sexo: [M/F] ')).upper()
while s != 'M' and s != 'F':
    s = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
print('Sexo {} registrado com sucesso.'.format(s)) """

""" Do Guanabara """

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))