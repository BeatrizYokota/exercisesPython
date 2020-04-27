salario = float(input('Digite o salário: '))
if salario >= 1250:
    aumento = salario + salario*0.10
else:
    aumento = salario + salario*0.15
print('Seu novo salário é de {} reais' .format(aumento))
