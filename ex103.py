def ficha (nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')


# Programa Principal
jogador = str(input('Nome do Jorgador: ')).upper()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    g = 0
if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)
