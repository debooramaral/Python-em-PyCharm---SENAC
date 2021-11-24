salarioFIXO = int(input('Quanto é o salario '))
vendas = int(input('Qual o valor das vendas '))
print('\n')
if vendas <= 20000:
    comissao1 = vendas * 0.04
    x = vendas + comissao1
    print('seu pagamento é de: ', salarioFIXO + x)
elif vendas > 20000:
    comissao2 = vendas * 0.05
    y = vendas + comissao2
    print('seu pagamento é de: ', salarioFIXO + y)
