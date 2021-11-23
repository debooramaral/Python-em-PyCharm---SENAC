print('Qual é o menor custo de combustivel da sua viagem \n')

km = int(input('Quantos KM vai percorrer? '))
vlg = int(input('Qual é o valor da Gasolina: '))
vla = int(input('Qual é o valor do Alcool: '))
consumog = int(input('Quantos o carro faz com o litro da Gasolina '))
consumoa = int(input('Quantos o carro faz com o litro de Alcool '))

print('\n')

calculo1 = km / consumog
calculo2 = km / consumoa

calculo3 = calculo1*vlg
calculo4 = calculo2*vla

if calculo3 > calculo4:
    print('a Gasolina é mais viável')
else:
    print('o Alcool é mais viável')
