m = int(input(f'Digite o 1 ° numero'))
maior = m
menor = m
for c in range(2,5):
    m = int(input(f'Digite o {c} ° numero'))
    if m > maior:
        maior = m
    if m < menor:
        menor = m
print(f'Maior {maior} e Menor {menor}')