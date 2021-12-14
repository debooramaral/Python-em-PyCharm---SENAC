print('PRESIDENCIA DO CLUBE\n')
firminio = 1
eugenia = 2
branco = 0
nulo = 9
i = contF = contE = somaF = somaE = contB = contN = voto = 0

for i in range (0,3):
    i = i + 1
    voto = int(input('Em quem deseja votar\n 1 - FIRMINIO \n 2 - EUGENIA \n 0 - VOTO BRANDO \n 9 - VOTO NULO \n~DIGITE SUA OPÇÃO AQUI: '))
    if voto == 1:
        contF += 1
    elif voto == 2:
        contE += 1
        if voto == 0:
            contB += 1
        elif voto == 9:
            contN += 1
print('\n______________________________________________RESULTADO !\n')
print('os votos de FIRMINIO são de', contF)
print('os votos de EUGENIA são de', contE)
print('os votos em BRANCO são de', contB)
print('os votos NULOS foram', contN)
print('O número total de ELEITORES que votaram são de', i)