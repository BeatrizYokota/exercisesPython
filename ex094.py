cadastro = {}
galera = []

soma = media = 0


while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    galera.append(cadastro.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar in 'NS':
            break
        print('Erro! Digite apenas S ou N')
    if continuar == 'N':
        break
print('-'*30)
print(f'Foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'A média de idade é {media:5.2f}')
print(f'As mulheres cadastradas são: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('A lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('         ')
        for k, v in p.items():
            print(f'{k} = {v}')
        print()
print('    == ENCERRADO ==')
