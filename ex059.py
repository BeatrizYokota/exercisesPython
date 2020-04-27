soma = 0
maior = 0
mult = 0
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] SOMA
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR''')

    opcao = int(input('Qual é sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma dos números {} e {} é {}' .format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação dos números {} e {} é {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre os números {} e {}, o maior deles é {}'.format(n1, n2, maior))
        else:
            maior = n2
            print('Entre os números {} e {}, o maior deles é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe novamente: ')
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif opcao == 5:
        print('Finalizando ...')
    else:
        print('Opção inválida. Tente novamente')
print('Fim do programa! Volte sempre!')