sexo = str(input('Digite o sexo [M/F]')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Digite o sexo [M/F]')).strip().upper()[0]
print('Sexo {} digitado com sucesso' .format(sexo))