time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for n in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {n+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['totalGols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Responda apenas com S ou N')
    if resposta == 'N':
        break
print('-'*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>2}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para finalizar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}')
    else:
        print(f'  == LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} ==')
        for i, v in enumerate(time[busca]['gols']):
            print(f'    => Na partida {i+1}, fez {v} gols')
    print('-'*30)
print('   << VOLTE SEMPRE >>')
