# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai  perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

''' Meu Programa '''

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos o senhor deseja pagar? '))
meses = anos * 12
salarioMin = (salario * 30) / 100
pMensal = casa / meses

if salarioMin <= pMensal:
    print('Sinto muito, mas o senhor não está apto para o empréstimo')
else:
    print('O senhor esta apto para o empréstimo!')

print('O valor da prestação mensal é de {:.2f}, em {} anos, o minimo é de {:.2f}'.format(pMensal, anos, salarioMin))

''' Do Guanabara '''

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')