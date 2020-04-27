media = 0
somaIdade = 0
idadeMaior = 0
contIdadeMenor = 0
nomeMaisVelho = 0
for c in range (1, 5):
    print('-----------   {}ª pessoa ------------' .format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        idadeMaior = idade
        nomeMaisVelho = nome
    if idade > idadeMaior and sexo in 'Mm':
        idadeMaior = idade
        nomeMaisVelho = nome
    if idade < 20 and sexo in 'Ff':
        contIdadeMenor += 1
media = somaIdade/4
print('A ideda média do grupo é {} anos' .format(media))
print('O homem mais velho tem {} anos e se chama {} ' .format(idadeMaior, nomeMaisVelho))
print('Ao todo são {} mulheres com menos de 20 anos' .format(contIdadeMenor))