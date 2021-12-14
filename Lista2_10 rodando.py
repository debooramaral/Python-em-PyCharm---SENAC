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

    s1 = float(input('O 1º salto, qual foi a distância: '))
    list.append(s1)
    s2 = float(input('O 2º salto, qual foi a distância: '))
    list.append(s2)
    s3 = float(input('O 3º salto, qual foi a distância: '))
    list.append(s3)
    s4 = float(input('O 4º salto, qual foi a distância: '))
    list.append(s4)
    s5 = float(input('O 5º salto, qual foi a distância: '))
    list.append(s5)
    print(list)
    print('\no MELHOR salto foi de: ',{max(list)})
    print('o PIOR salto foi de: ',{min(list)})

    if {max(list)} and {min(list)}:
        x = sum(list)
        y = x - max(list) - min(list)
        z = y / 3
        media = z
        print('\na media dos demais saltos, é de:', media, 'M')
    break
print('\nENCERRADO, por favor coloque o nome do atleta!')










