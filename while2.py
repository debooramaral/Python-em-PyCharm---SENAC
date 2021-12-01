cont = 1 #contador para dar inicio a contagem, o incremento
soma = 0
while cont <= 10: #aqui ele não diz respeito ao número 10, mas sim as 10x
    x = int(input('{} Digite o número '.format(cont)))
    soma += x #o que significa += ?
    cont = cont + 1 #não sabia que esta operação funcionava aqui
    media = soma / 10

print('a MÉDIA destes número é:', media) #como deixar esta média em formato de número inteiro
