v = int(input('Digite um Número: '))
s = 0
for c in range(1,v+1):
    soma = s + c
    print(soma)
    s = soma
print('a soma, em sequencia do número inserido é de: ', soma)