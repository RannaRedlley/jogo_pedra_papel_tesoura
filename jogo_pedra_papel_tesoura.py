print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

rodadas = 0
pontos_jogador1 = 0
pontos_jogador2 = 0
empate = 0

while True:
    jogada_jogador1 = ''
    jogada_jogador2 = ''
    while True:
        jogador1 = input('Jogador 1 qual é a sua escolha? ').lower()
        if jogador1 == 'pedra' or jogador1 == 'papel' or jogador1 == 'tesoura':
            jogada_jogador1 = jogador1
            break
        else:
            print('Digite o nome de uma das opções apresentadas!')
            continue

    while True:
        jogador2 = input('Jogador 2 qual é a sua escolha? ').lower()
        if jogador2 == 'pedra' or jogador2 == 'papel' or jogador2 == 'tesoura':
            jogada_jogador2 = jogador2
            break
        else:
            print('Digite o nome de uma das opções apresentadas!')
            continue

    if jogada_jogador1 == jogada_jogador2:
        empate += 1
        rodadas += 1
        print('Empate')
        if rodadas == 3:
            break
        else:
            continue

    elif (jogador1 == 'tesoura' and jogador2 == 'papel') or \
            (jogador1 == 'pedra' and jogador2 == 'tesoura') \
            or (jogador1 == 'papel' and jogador2 == 'pedra'):
        print('Jogador 1 venceu a partida')
        pontos_jogador1 += 1
        rodadas += 1
        if rodadas == 3:
            break
        else:
            continue

    elif (jogador2 == 'tesoura' and jogador1 == 'papel') or \
            (jogador2 == 'pedra' and jogador1 == 'tesoura') \
            or (jogador2 == 'papel' and jogador1 == 'pedra'):
        print('Jogador 2 venceu a partida')
        pontos_jogador2 += 1
        rodadas += 1
        if rodadas == 3:
            break
        else:
            continue

if pontos_jogador1 > pontos_jogador2:
    print('O jogador 1 venceu o jogo!')
elif pontos_jogador2 > pontos_jogador1:
    print('O jogador 2 venceu o jogo!')
else:
    print('Ambos tiveram a mesma pontuação, portanto EMPATE')