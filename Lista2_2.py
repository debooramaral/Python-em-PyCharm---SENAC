num = 0
cont = 0
while cont >= 0:
    num = int(input('Digite um número '))
    cont = cont + 1
    if num == -1:
        cont += num
        print('\nF I M')
        print('\nOs números digitados foram: ', cont)
        break
