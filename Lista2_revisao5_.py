num = int(input('Digite um número '))
maior = num
menor = num
for i in range(2,5):
    num = int(input(f'Digite o {i}º número '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print('o maior número é', maior, 'e o menor número é', menor)


