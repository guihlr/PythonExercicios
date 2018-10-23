# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros


print('{:=^40}'.format(' LOJAS GUILHERME '))
compras = float(input('Preço das compras: R$'))
print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista do cartão
[ 3 ] em ate 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    desconto = compras - (compras * 10 / 100)
    print('À vista dinheiro/cheque, sua compra com 10% de desconto, R${:.2f}'.format(desconto))
elif opcao == 2:
    desconto = compras - (compras * 5 / 100)
    print('À vista no cartão, sua compra com 5% de desconto, R${:.2f}'.format(desconto))
elif opcao == 3:
    desconto = compras
    parcela = compras / 2
    print('Você ira parcelar em 2x de {:.2f}'.format(parcela))
    print('Em até 2x no cartão, preço normal, R${:.2f}'.format(desconto))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = compras + (compras * 20 / 100)
    parcelado = juros / parcelas
    print('Sua compras parcelado em {}x de {:.2f} COM JUROS'.format(parcelas, parcelado))
    print('3x ou mais no cartão, sua compra com 20% de juros, R${:.2f}'.format(juros))
else:
    print('Opção Inválida! Tente novamente.')
