# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
from time import sleep

vel = float(input('Digite a velocidade em que estava dirigindo: '))
if vel > 80:
    multa = (vel - 80) * 7 # - 80 pq o limite ja é de 80 e ele não paga multa se estiver abaixo de 80!
    print('Você foi multado por ultrapassar o limite de 80Km/h')
    print('CALCULANDO MULTA...')
    sleep(1)
    print('Sua multa é de R${:.2f}'.format(multa))
else:
    print('voce nao foi multado!')
