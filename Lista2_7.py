from getpass import getpass

num = int(getpass('Digite o numero a ser adivinhado: '))

cont = 0
while True:
    chute = int(input('Digite seu numero:'))
    if chute > num:
        print('Tente um numero mais baixo')
    elif chute < num:
        print('Tente um numero mais alto')
    else:
        print(f'Parabens voce acerto em {cont} tentativas')
        break
    cont = cont + 1