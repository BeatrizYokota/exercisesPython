nome = str(input('Digite uma frase: ')).strip().upper()
palavras = nome.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)  - 1, -1, -1):
    inverso += junto[letra]
    if inverso == junto:
        print('Temos um palídromo!')
print('Você digitou a frase {} e o inverso dela é {}' . format(junto, inverso))