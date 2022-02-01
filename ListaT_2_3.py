def contador():
    for q in range (quant):
        cont = q * 1.99
        print(f'{q + 1}\t\t{1.99 * (q + 1)}')


def linha():
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬')


print('\t\tLoja Quase DOIS\n')
quant = int(input('Quantos produtos esta comprando? '))
valor = quant * 1.99
print(f'\n\t\t**   CUPOM \t**\n\t\tITENS\t\tR$\n\t\t{quant} {valor:>14.2f}\n\nObrigada e até mais!\n')
linha()
contador()
