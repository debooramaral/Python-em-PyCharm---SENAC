import os
lista = []
i = int
while True:
    
    num = int(input('Digite um  numero diferente de 0: '))

    if num == 0:
        break
    lista.append(num)

Vm = sum(lista)/len(lista)

os.system('cls')

print(f'Quantidade de valores inseridos: {len(lista)}')

print(f'Valores inseridos: {lista}')

lista.reverse()
print(f'Valores em ordem inversa {lista}')

print(f'Soma de todos os valores: {sum(lista)}')

print(f'Media:{Vm:.1f}')

print(f'Valores acima da media: {sum(i > Vm for i in lista)}')

print(f'Valores abaixo de sete: {sum(i < 7 for i in lista)}')

print('Programa encerrado  ( ͡° ͜ʖ ͡°)')
