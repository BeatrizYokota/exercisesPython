print('Gerador de PA')
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> ' .format(termo), end = '')
        termo += r
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
print('Progressão finalizada com {} termos mostrados' .format(total))