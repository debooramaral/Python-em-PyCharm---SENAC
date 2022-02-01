print('\tHIPERMERCADO TABAJARA\n')
print(f'\t\t\t\t\tAté 5Kg\t\t\t\tAcima de 5 Kg\n1.File Duplo\t\tR$4,90 por Kg\t\tR$5,80 por Kg\n2.Alcatra\t\t\tR$5,90 por Kg\t\tR$6,80 por Kg\n3.Picanha\t\t\tR$6,90 por Kg\t\tR$7,80 por Kg\n')

def carnes(tipo,quant,kg):

    tipo = input('Que tipo de carne você comprou? ')
    quant = int(input('Qual a quantidade de carne que você comprou? '))
    kg = input('A compra é de até 5 Kg ou acima de 5 Kg. Responda até ou acima! ')
    #print(f'\t A carne é _{tipo}_, com a quantidade de _{quant}_ e tem os valores, correspondente a _{kg}_')
carnes(tipo = 0, quant = 0, kg = 0) #porque isso?

cartao = int(input('Você utilizou o cartão Tabajara? \n1 - sim\t 2 - não\t\tDigite: '))


