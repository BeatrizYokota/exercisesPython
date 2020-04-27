valor = float(input("Valor da compra: R$ "))
print('''Digite a opção de pagamento que deseja:
1 - A vista no dinheiro/cheque
2 - A vista no cartão
3 - Parcelado em até 3x
4 - Parcelado em 3x ou mais''')
opcaoPagamento = int(input("Opção escolhida: "))

if opcaoPagamento == 1:
    total = valor - valor*0.10
    print('O valor a ser pago a vista no dinheiro/cheque é R${:.2f}' .format(total))
elif opcaoPagamento == 2:
    total = valor - valor*0.05
    print('O valor a ser pago a vista no cartão é R$ {:.2f}' . format(total))
elif opcaoPagamento == 3:
    total = valor
    parcela = total / 2
    print('O valor a ser pago parcelado em 2x no cartão é R$ {:.2f} SEM JUROS'.format(parcela))
elif opcaoPagamento == 4:
    total = valor + valor*0.20
    totalParcelas = int(input('Quantas parcelas? '))
    parcela = total / totalParcelas
    print('O valor a ser pago parcelado em {}x no cartão é R$ {:.2f} COM JUROS'.format(totalParcelas, parcela))
else:
    print("Essa opção não existe!")
