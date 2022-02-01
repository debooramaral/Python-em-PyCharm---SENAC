peso_P = excesso_P = excesso = 0
listaE = []
while True:
    peso_P = int(input('Quanto de peixe foi pescado? KG '))
    excesso_P = (peso_P - 50) * 4
    print(f'\tvalor da multa R$ {excesso_P}')
    excesso = peso_P - 50
    listaE.append(excesso)
    print(f'\tquantidade de KG {excesso}')
    print('\n')




