# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

funcionario = float(input('Qual é o salário do funcionário? R$ '))
if funcionario <= 1250:
    salario = funcionario + (funcionario * 15) / 100
else:
    salario = funcionario + (funcionario * 10) / 100
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(funcionario, salario))
