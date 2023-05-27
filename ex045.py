from random import randint
from time import sleep
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j = int(input('Qual é a sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('=-'*20)
print('O computador escolheu {}'.format(itens[pc]))
print('O jogador jogou {}'.format(itens[j]))
print('=-'*20)
if pc == 0: #pedra
    if j == 0:
        print('EMPATE')
    elif j == 1:
        print('JOGADOR VENCE')
    elif j == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif pc == 1:#papel
    if j == 0:
        print('JOGADOR VENCE')
    elif j == 1:
        print('EMPATE')
    elif j == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif pc == 2: #tesoura
    if j == 0:
        print('JOGADOR VENCE')
    elif j == 1:
        print('COMPUTADOR VENCE')
    elif j == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')