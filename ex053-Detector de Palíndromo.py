# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).upper().strip()  # Le a frase, coloca em maiusculo, tira os espaços(comeco,fim)
palavras = frase.split()  # "splitou", para gerar uma lista
junto = ''.join(palavras)  # junta as listas para eliminar os espaços ('aspas sem espaços'.join),junta em uma string só

# Inverso da lista (string)
#inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, - 1, - 1):  # da ultima letra (-1), até a primeira (-1), voltando uma letra (-1)
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:  # se o inverso for o mesmo que o junto, temos um palíndromo
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
