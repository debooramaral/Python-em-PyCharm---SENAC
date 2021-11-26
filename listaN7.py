print('BRECHÓ\n')
aquisicao = int(input('Qual o valor de aquisição do produto '))

if aquisicao <= 50:
    x = (aquisicao * 0.45) + aquisicao
    print('Este produto será vendido a $ ',x)
else:
    y = (aquisicao * 0.30) + aquisicao
    print('O produto sera vendido a $ ', y)