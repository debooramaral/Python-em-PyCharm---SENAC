num = 0
impar = 0
soma = 0
while num != -999:
    num = int(input('Digite números impares, pode iniciar com -999 '))
    if num < 0:
        impar = impar + 1
        soma = num + impar
    else:
           break

print('\nos números impares foram ', impar)