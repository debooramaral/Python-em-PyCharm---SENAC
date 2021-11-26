print('DESCRIÇÃO DA VENDA \nInsira a quantidade de camisetas \n')
camiP = int(input('~  Pequenas '))
camiM = int(input('~  Médias '))
camiG = int(input('~  Grandes '))

p = 10
m = 12
g = 15

vt = (camiP * p) + (camiM * m) + (camiG * g)

print('\no Valor Total da sua compra é de: $ ', vt)