from datetime import datetime

trabalhador = {}
idade = 0

trabalhador['nome'] = str(input('Nome: '))
nascimento = int(input(f'Ano de Nascimento: '))
trabalhador['idade'] = datetime.now().year - nascimento
trabalhador['ctps'] = int(input('Número da carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year)
    trabalhador['salário'] = float(input('Salário: R$ '))
print('-'*30)
for k, v in trabalhador.items():
    print(f'    - {k} tem o valor {v}')