from tkinter import *

ModeloJanela = Tk()


def telaBase():
    ModeloJanela.title('PRIMEIRA TELA')
    ModeloJanela.configure(background='cyan')
    # ModeloJanela.geometry('788x589')
    # ModeloJanela(True,True)
    ModeloJanela.maxsize(width=1024, height=789)
    ModeloJanela.minsize(width=489, height=399)

'''frame = LabelFrame(ModeloJanela, text='~~', bg='CYAN', font=(10))
frame.pack(expand=True, fill=BOTH)'''

def eventhandler(mensagem):
    print(mensagem)


def botao():
    bot = Button(ModeloJanela, text='CLIQUE AQUI', fg='black', bg='pink', command=lambda:eventhandler('Oi'))
    bot.place(relx=0.2, rely=0.1, relwidth=0.25, relheight=0.10)
    '''bot.pack() #outra opção de botão !'''


def menus():
    barramenu = Menu(ModeloJanela)
    ModeloJanela.configure(menu=barramenu)

    mn1 = Menu(barramenu, tearoff=0)
    barramenu.add_cascade(label='Versão', menu=mn1)
    mn1.add_command(label='Sobre')
    mn1.add_separator()
    mn1.add_command(label='Sair')


telaBase()
menus()
botao()

ModeloJanela.mainloop()
