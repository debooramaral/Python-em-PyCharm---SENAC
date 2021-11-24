print('TRABALHANDO FELIZ\n')

salario = int(input('Insira o salário '))

aumento1 = 0.02
aumento2 = 0.01

if salario <= 2000:
    x = salario * aumento1
    salarioFinal1 = salario + x
    print('seu rendimento é de', salarioFinal1, 'Com AUMENTO DE 20%')
elif salario >= 2000:
    y = salario * aumento2
    salarioFinal2 = salario + y
    print('seu rendimento é de ', salarioFinal2, 'Com AUMENTO DE 10%')