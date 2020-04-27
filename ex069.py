contVinte = contSexo = contMaior = 0

print('-' * 30)
while True:
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    continuar = ' '
    if idade >= 18:
        contMaior += 1
    if sexo == 'M':
        contSexo += 1
    elif sexo == 'F' and idade < 20:
        contVinte += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' *30)
print(f'Foram cadastradas {contMaior} pessoas acima de 18 anos')
print(f'Foram cadastrados {contSexo} homens')
print(f'Foram cadastradas {contVinte} mulheres com menos de 20 anos')
