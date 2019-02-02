# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
gols = list()
tot = 0

dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for p in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))
    dados['gols'] = gols
for qtd in gols:
    tot += qtd
    dados['total'] = tot
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for p, g in enumerate(dados['gols']):
    print(f'    => Na partida {p + 1}, fez {g} gols.')
print(f'Foi um total de {tot} gols.')
