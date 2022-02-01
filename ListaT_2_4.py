def ValorPagamento():
    juros = dia * 0.001
    multa = prestação * 0.03
    valor_conta = prestação + multa + juros
    print(f'\t\t\tO valor a ser pago é de: {valor_conta:.2f}')


valor_conta = multa = juros = cont = 0
somaVP = [] #quero somar o que tem dentro do def . . .
print('Digite ZERO pra sair!\n')
while True:
    prestação = float(input('Qual é o valor da prestação? '))
    somaVP.append(prestação) #é mesmo necessário ?
    if prestação == 0:
        break
    dia = int(input('Quantos dias de atraso, desde o vencimento? '))
    ValorPagamento()
    cont = cont + 1

print(f'\t\t\nRELATÓRIO DO DIA\nQuantidade de Contas Pagas no dia: {cont}\nValor Total de Prestações Pagas no dia: {sum(somaVP)}')

