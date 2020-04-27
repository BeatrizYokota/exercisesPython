from datetime import date
atual = date.today().year
contMaior = 0
contMenor = 0
for c in range (1, 8):
    ano = int(input('Digite o ano de nacimento: '))
    idade = atual - ano
    if idade >= 18:
        contMaior += 1
    else:
        contMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} pessoas menores de idade.'.format(contMaior, contMenor))