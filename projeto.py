import random

times = ['atletico mineiro', 'flamengo', 'corinthians', 'botafogo', 'vasco', 'internacional']
saldo = 0

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
        print('depósito é 1')


   