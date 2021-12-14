num = int(input(f'Digite um número')) #por que o f ?
num = 0
maior = num
menor = num
for i in range (2,5):
    num = int(input(f'Digite mais um número', {i})) # por que ele tem que estar entre chave {}
    if num > maior:
        maior = num
    if num != 0 and menor:
        menor = num
print('o maior número é', maior, 'e o menor número é', menor)


