def linha ():
    print('_'*32)


print('\tHIPERMERCADO TABAJARA\n')
print(f'\t\t\t\tAté 5Kg\t\t\t\tAcima de 5 Kg\nFile Duplo\t\tR$4,90 por Kg\t\tR$5,80 por Kg\nAlcatra\t\t\tR$5,90 por Kg\t\tR$6,80 por Kg\nPicanha\t\t\tR$6,90 por Kg\t\tR$7,80 por Kg\n')
carne =  compra = pagamento = total = 0
tipo = input('Que tipo de carne você deseja? ').upper()
quant = int(input('Qual a quantidade de carne que quer comprar? KG '))

if tipo == 'FILE DUPLO':
    if quant <= 5: carne = quant * 4.90
    if quant >= 5: carne = quant * 5.80
if tipo == 'ALCATRA':
    if quant <= 5: carne = quant * 5.90
    if quant >= 5: carne = quant * 6.80
if tipo == 'PICANHA':
    if quant <= 5: carne = quant * 6.90
    if quant >= 5: carne = quant * 7.80

#print(f'\tA carne {tipo} com {quant} Kg, esta custando R$ {carne:.2f}')

cartao = input('A forma de pagamento é com o Cartão Tabajara? \nSim\nNão\nDigite: ').upper()
if cartao == 'SIM':
    compra = (carne * 0.95)
if cartao == 'NÃO':
    pagamento = input('Que tipo de pagamento vai realizar:\nDinheiro\nOutro Cartão\nPix\nDigite: ').upper()

#print(f'A mercadoria recebeu 5% de desconto, total a pagar R$ {compra:.2f}')

if total > 0:
    total = compra #o que colocar aqui? para aplicar o desconto . .
else:
    total = carne

linha()
print('\t\t\tCUPOM FISCAL')
linha()

print(f'\nItens\t\t\t\t\t\t R$\nCarne:{tipo:>10}{carne:>16,.2f}\nCartão Tabajara: {cartao}\n\t5% OFF\t{compra:>20,.2f}\nPagamento: {pagamento:>21}\n\t\tTotal a Pagar: {total:>9,.2f}')
linha()
