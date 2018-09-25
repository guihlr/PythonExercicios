# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

func = float(input('Digite o seu salário: '))
sal = func+(func*15/100)
print(f'Seu salario com 15% de aumento é de {sal:.2f}')
