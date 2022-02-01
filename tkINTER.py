from tkinter import  *

def teste_da_janela ():
    print('Olá Mundo!')
    nome = input('Qual é o seu nome: ')
    print(f'seja bem vind@ {nome:^15} !')

janela = Tk() # criação de janela
janela.title('\t\tDébora') # titulo
janela.geometry('400x400') # determina o tamanho da janela
# portanto pode-se brincar entre os eixos e a geometria para organizar a janela

texto_orientação = Label(janela, text='clique no botão para exibir') # pedaço de texto dentro de uma janela (Label); o parametro é passar qual janela esta se referindo e descrever o texto que deseja mostrar
texto_orientação.grid(column=0, row=0, padx=10, pady=10) # determina em que linha e coluna quer que seu texto esteja aparecendo

texto_orientação2 = Label(janela, text='sei la')
texto_orientação2.grid(column=1, row=3, padx=10, pady=10)

botão = Button(janela, text='buscar', command = teste_da_janela) # cria botão, utilizando o button, insira o texto na sequencia, depois coloque o comando "def' por exemplo (olhar os passos)
# () parenteses na def, executa agora a função no def, sem o parenteses, só executara quando clicar em um botão especifico
botão.grid(column=2, row=4)

texto_orientação3 = Label(janela, text='') # texto vazio cria-se uma linha na posição determinada no grid
texto_orientação3.grid(column=0, row=1)
# o texto feito no código e printado para mostrar as informações desejadas, precisa estar entre colchete, aquele usado na lista [] com o 'text' dentro e = a variavel que chamou o texto feito
# por exemplo: texto_desejado[text] = texto_desejado
# portando passa a exibir o texto no centro da janela
# para separa as linhas dentro da janela, utiliza-se espaços entre os eixos x e y ~> padx= e pady=, teste valores, lá no grid

janela.mainloop() # termina! exiba e permaneça exibindo



''' Primeiro passo: importar o tk inter
    Segundo passo: coloque seu código dentro de uma função, sem parametros, para postereiormente passar ao botão a função desejada
    Terceiro passo: crie sua janela usando o tk inter
    
    como eu faço para dar um duplo clique no arquivo e logo abrir a janela e o código ser executado? transforme o código em um arquivo executavel. VEJA OUTRO VIDEO DO ~> Hashtag Programação'''
