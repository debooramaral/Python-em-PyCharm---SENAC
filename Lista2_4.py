num = 0
cont = 0
while cont >= 0:
    num = int(input('Digite um número '))
    if num == 50:
        cont = cont + 1
    elif num == 0:
        print('\nO número   ~ 50 ~   apareceu: ', cont)
        break