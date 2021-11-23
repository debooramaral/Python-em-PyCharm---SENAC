salariofixo = int(input('Qual é o valor do salario: '))
vendas = int(input('Qual valor das suas vendas: '))

comissao1 = 0.04
comissao2 = 0.05

if vendas > 20000:
        print('seu salario final é: ', (vendas * comissao2)+salariofixo)
elif vendas <= 20000:
    print('seu salario final é: ', (vendas * comissao1)+salariofixo)
