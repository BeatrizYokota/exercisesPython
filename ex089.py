turma = []
aluno = []

media = 0

while True:
    nome = str(input('Nome: ')).strip().upper()
    n1 = float(input('Nota 1 : '))
    n2 = float(input('Nota 2 : '))
    media = (n1 + n2)/2
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)
    turma.append(aluno[:])
    aluno.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i,a in enumerate(turma):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    notaAluno = int(input('Deseja imprimir as notas de qual aluno? (DIGITE 999 PARA FINALIZAR) '))
    if notaAluno == 999:
        print('Finalizando ...')
        break
    if notaAluno <= len(turma):
        print(f'As notas do aluno {turma[notaAluno][0]} foram {turma[notaAluno][1]} e {turma[notaAluno][2]}')
