# Fatiamento
# Fatiar uma 'string' é conseguir pegar pedaços dela.
# O simbolo de colchetes [] é o identificador de uma estrutura de dado do python, chamada lista.
# O Python diferencia letras Maiusculas de minusculas.

# Análise
# analisar uma 'string' é saber algumas informações sobre, como, qual tamanho, qual letra começa, qual termina, qual é a
# primeira palavra inteira e etc.
# utilizar a método/função 'len', len de 'length' ou 'comprimento'
# exemplo1: frase = 'test' /n print(len(frase)) = 4
# outra forma de analisar a string é utlizando o '.count'
# exemplo2: frase = 'test' /n print(frase.count('t'), ele ira contar quantas vezes aparece a letra 't'
# frase.find('deo')
# ('Curso' in frase), operador para True/False

# Transformação
# frase.replace('Python', 'Android')
# frase.upper() = maiusculas
# frase.lower() = minusculas
# frase.capitalize() = coloca tudo em minusculo menos a primeira letra Maiscula
# frase.title() = coloca cada primeira letra de uma string em maiuscula
# frase.strip() = vai remover todos os espaços inuteis no inicio e no final da string
# frase.rstrip() = remove os espaços da direito
# frase.lstrip() = remove os espaços da esquerda

# Divisão
# frase.split() = divide uma string em uma lista
# Junção
# '-'.join(frase) = junção, ex: junta oque foi splitado por "frase.split()"

frase = 'Curso em Video Python'
print(frase)
