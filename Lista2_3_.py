n = 0
m = 0
while n != -999:
    n = int(input('Digite um numero diferente de -999:'))
    if n == -999:
        break
    elif not(n == n %2 == 0):
         m +=1
print('Numeros ímpares digitados:', m)