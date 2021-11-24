print('CUSTO DA VIAGEM\n')
km = int(input('Quanto KM de viagem '))
print('\n')
vlG = int(input('Quanto custa a gasolina '))
consumoG = int(input('Quanto faz com um litro '))
print('\n')
vlA = int(input('Quanto custa o alcool '))
consumoA = int(input('Quanto faz com um litro '))
print('\n')

x = km / consumoG
y = km / consumoA

w = x * vlG
z = y * vlA

if w > z:
    print('Gasolina é mais viável\n')
else:
    print('Alcool é mais viável\n')

