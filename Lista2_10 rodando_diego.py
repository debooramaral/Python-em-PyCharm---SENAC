#cada atleta 5 saltos
#melhor e pior resultados eliminados
#media de 3 valores restantes
#Nome, 5 distancias dos saltos, media dos saltos
#use LISTA para armanezar os saltos
#os saltos são em ordem da execução, desordenados
#ENCERRA, quando nao é informado o nome do atleta
"""SAIDA, do programa conforme: Atleta: Rodrigo Curvêllo - Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m - Terceiro Salto: 6.2 m - Quarto Salto: 5.4 m
Quinto Salto: 5.3 m - Melhor salto:  6.5 m - Pior salto: 5.3 m
Média dos demais saltos: 5.9 m - Resultado final: Rodrigo Curvêllo: 5.9 m"""

list = []
media = x = y = z = 0

nome = (input('Qual é o seu nome '))
while nome != "":
    for i in range(1,6):
        salto = float(input(f'O {i}º salto, qual foi a distância: '))
        list.append(salto)
    print(list)
    print('\no MELHOR salto foi de: ',{max(list)})
    print('o PIOR salto foi de: ',{min(list)})

    x = sum(list)
    y = x - max(list) - min(list)
    z = y / 3
    media = z
    print(f'\na media dos demais saltos, é de: {media:.1f} M')
    #f de formatar | chaves daquilo que eu quero mudar | o valor da variavel (que eu coloco) | : alterar a variavel para . que quer dizer apenas uma casa decimal(modifico a variavel) e f, de float

#    break
    nome = (input('Qual é o seu nome ')) # porque fazer a leitura aqui de novo?, para entrar no laço e ler, vazio, para encerrar

#print('\nENCERRADO, por favor coloque o nome do atleta!')
print('\nENCERRADO')









