num = int(input("Digite um número inteiro: "))
print('''Escolha qual base de conversão você deseja:
1 - Binário
2 - Octal 
3 - Hexadecimal''')
opcao = int(input("Base de conversão escolhida: "))
if opcao == 1:
    print('{} convetido para BINÁRIO é igual a {}' .format(num, bin(num) [2:]))
elif opcao == 2:
    print('{} convertido em OCTAL é igual a {}' .format(num, oct(num) [2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}' .format(num, hex(num) [2:]))
else:
    print("Valor digitado está incorretp")