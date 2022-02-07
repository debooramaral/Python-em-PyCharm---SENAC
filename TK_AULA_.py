from tkinter import *

ModeloJanela = Tk()

def telaBase():
    ModeloJanela.title('PRIMEIRA TELA')
    ModeloJanela.configure(background='cyan')
    # ModeloJanela.geometry('788x589')
    # ModeloJanela(True,True)
    ModeloJanela.maxsize(width=1024, height=789)
    ModeloJanela.minsize(width=489, height=399)

telaBase()

def botao():
    bot = Button(ModeloJanela, text='CLIQUE AQUI')
    bot.place(relx=0.2, rely=0.1, relwidth=0.25, relheight=0.10)

botao()

def menu():
    
    menu.add_cascade(Label='CADASTRO', menu=menu)
    menu.add_command(Label='NOVO')
    menu.add_separator()

menu()

ModeloJanela.mainloop()
