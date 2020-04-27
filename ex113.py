def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um valor inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um valor inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número\033[m')
        else:
            return n

# Função Principal

n1 = leiaInt('Digite um valor Inteiro: ')
n2 = leiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
