# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

""" Meu Programa """

from time import sleep

# val1 = int(input('Primeiro valor: '))
# val2 = int(input('Segundo valor: '))
# opcao = 0
# while opcao < 5 or opcao > 5:
#     print('''    [ 1 ] somar
#     [ 2 ] multiplicar
#     [ 3 ] maior
#     [ 4 ] novos números
#     [ 5 ] sair do programa
# ''', end='')
#     opcao = int(input('>>> Qual é a sua opção? '))
#     print('=-==-=' * 5)
#     if opcao == 1:
#         soma = val1 + val2
#         print('A soma entre {} + {} é = {}'.format(val1, val2, soma))
#         sleep(2.5)
#     elif opcao == 2:
#         multiplicar = val1 * val2
#         print('O resultado de {} x {} é = {} '.format(val1, val2, multiplicar))
#         sleep(2.5)
#     elif opcao == 3:
#         if val1 > val2:
#             maior = val1
#         else:
#             maior = val2
#         print('Entre {} e {} o maior é = {}'.format(val1, val2, maior))
#         sleep(2.5)
#     elif opcao == 4:
#         sleep(1)
#         print('Informe os números novamente: ')
#         val1 = int(input('Primeiro valor: '))
#         val2 = int(input('Segundo valor: '))
#     else:
#         print('Opção Inválida. Tente novamente.')
#         sleep(1)


''' Do Guanabara '''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finaliazndo...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa. Volte sempre!')
