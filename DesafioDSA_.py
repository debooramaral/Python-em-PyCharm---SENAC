pontos = total = 0
livroS = 0
nome = str

clientes = [['anderson', 4]]
#clientes = [['anderson', 4], ['Debora', 2]]


def npontos(clientes, nome, pontos):
    for indice, cliente in enumerate(clientes):
        if cliente[0] == nome:
            cliente[1] += pontos
            print(cliente)
        else:
            clientes.append([nome, pontos])


print(f'\t\t\tLIVRARIA\n')

while True:

    nome = input('Qual seu nome: ')
    livroS = int(input('Quantos livros você comprou: '))

    if livroS == 1:
        pontos += 5
        print(f'você tem {pontos}')
    if livroS == 2:
        pontos += 15
        print(f'você tem {pontos}')
    if livroS == 3:
        pontos += 30
        print(f'você tem {pontos}')
    if livroS >= 4:
        pontos += 60
        print(f'você tem {pontos}')
    if livroS == 0:
        break
    npontos(clientes, nome, pontos)


