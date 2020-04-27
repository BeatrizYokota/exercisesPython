casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = float(input("Em quantos anos você vai pagar? "))
prestacao = casa/(anos*12)
limitePrestacao = salario*0.30
if prestacao > limitePrestacao:
    print("Infelizmente não será possível comprar a casa")
elif prestacao <= limitePrestacao:
    print("Empréstimo aprovado! Suas prestações serão de {} reais" .format(prestacao) )
