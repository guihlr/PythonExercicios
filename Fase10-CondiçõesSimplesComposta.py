# Estruturas Sequenciais: De cima para baixo sem possibilidade de mudança.
# if: else: - Estrutura Condicional
# if: Bloco True
# else: Bloco False

# Estrutura Condicional :

# if carro.esquerda():
#   Bloco True
# else:
#   Bloco False

# Somente if:, para estrutura Simples e if: else:, para estrutura Composta.

# T0do comando que estiver colado do lado esquerdo da tela. vai ser executado sempre e aquele comando que estiver com
# indentação para dentro(alinhado no bloco), ele pode ser ou não executado.

# Estrutura Condicional:

""" tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--') """

# Condição Simplificada:

tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

# Ao inves de usar bloco if: else:, eu simplifiquei colocando no print. Isso apenas para um if: else:.
