import random

times = ['atletico mineiro', 'flamengo', 'corinthians', 'botafogo', 'vasco', 'internacional']
saldo = 100

while True:
    print('================================\n' \
          'Bem-vindo a plataforma MEGbet\n' \
          'como podemos ajudar?\n'\
          '1. Depositar\n2. Sacar\n3. Apostar\n4. Saldo\n5. Sair\n' \
          '================================\n')

    comando = int(input('registre-se: '))

    if comando == 1:
        deposito = float(input("valor a ser depositado: "))
        saldo+=deposito

    elif comando == 2:
        saque = float(input('saque: '))
        if saque > saldo:
            print('Operação inválida!')
        else:
            saldo -= saque
            print(f'Saque realizado! Valor do saque: {saque}')


   
