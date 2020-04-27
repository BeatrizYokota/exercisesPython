def voto(nascimento):
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if idade < 16:
        print(f'Com {idade} anos: Voto NEGADO')
    elif 16 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos: Voto OPICIONAL')
    elif idade >= 18:
        print(f'Com {idade} anos: Voto OBRIGATÓRIO')


# Programa Principal
print('-'*20)
ano = int(input('Digite o ano de nascimento: '))
voto(ano)