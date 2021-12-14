menorF = 999999999999
maiorF = cont = contM = mediaF = mediaT = soma = somaM = 0
for i in range(1,7):
    sexo = input('Qual é o sexo M - Masculino e F - Feminino ')
    altura = float(input('Qual é sua altura '))

    if sexo == "F":
        cont = cont + 1
        if altura > maiorF:
            maiorF = altura

        if altura < menorF:
            menorF = altura

        soma = soma + altura
        mediaF = soma/cont

    elif sexo == "M":
        contM = contM + 1
        somaM = somaM + altura

soma = soma + somaM
cont = cont + contM

mediaT = soma/cont

print('\na maior altura das mulheres', maiorF)
print('a menor altura das mulheres', menorF)
print('\na media da altura das mulheres', mediaF) #FORMATAR A SAIDA
print('\na media da altura da turma', mediaT) #FORMATAR A SAIDA
