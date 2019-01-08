# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
          'Atlético-MG', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
          'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
          'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')

print('-=-' * 10)
print(f'Os 5 primeiros colocados são : {tabela[:5]}')
print('-=-' * 10)
print(f'Os últimos 4 colocados são: {tabela[16:20]}')
print('-=-' * 10)
print(f'Times em ordem alfabética: {sorted(tabela)}')
pos = tabela.index('Chapecoense')
print('-=-' * 10)
print(f'O time Chapecoense está na {pos+1}ª posição')
