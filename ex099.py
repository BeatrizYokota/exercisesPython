from time import sleep

def maior(*num):
    print('-='*30)
    print('Analisando os valores passados ...')
    sleep(0.5)
    maiorValor = cont = 0
    for n in num:
        print(f'{n} ', end='', flush=True)
        sleep(0.25)
        if cont == 0:
            maiorValor = n
        else:
            if n > maiorValor:
                maiorValor = n
        cont += 1
    print(f'\nForam informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maiorValor}')


# PROGRAMA PRINCIPAL
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()