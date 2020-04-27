from datetime import date
atual = date.today().year
ano = int(input("Digite o ano de nascimento: "))
idade = atual - ano
if idade < 18:
    prazo = 18 - idade
    print("Você ainda vai se alistar em {} anos" .format(prazo))
elif idade == 18:
    print("Você deve ser alistar esse ano")
elif idade > 18:
    prazo = idade - 18
    print("Já passou o tempo do alistamento em {} anos" .format(prazo))
