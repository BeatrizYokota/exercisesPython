palavras = ('aprender', 'limpar', 'ensinar', 'comer', 'programar',
            'gratis', 'futuro', 'trabalhar', 'curso')
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='')
