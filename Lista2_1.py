n = 0
m = 0
while n != -999:
    n = int(input('Digite um numero diferente de -999:'))
    if n == -999:
        break
    else:
        m = n
        s = n + m

print('Soma dos numeros digitados:', s)