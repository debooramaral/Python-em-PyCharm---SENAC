from tkinter import *
import requests

def bemvindo ():
    t4.config(text = 'http://www.megamensagens.com/gifs/recados-gifs-de-bem-vindo/gifs-de-bem-vindo00251/')

janela = Tk()
janela.configure(background='white')
janela.title('AMARAL - a mais maravilhosa :D')
janela.geometry('500x600')

t1 = Label(janela, text='OPÇÃO', background='beige')
t1.grid(column=10, row=10, padx=5, pady=5)

t2 = Label(janela, text='TESTE', background='beige')
t2.grid(column=20, row=10, padx=5, pady=5)

t3 = Label(janela, text='PROGRAMA', background='beige')
t3.grid(column=30, row=10, padx=5, pady=5)

t4 = Label(janela, text='zzzzzzzzzzzzzzzzz')
t4.grid(column=50, row=20, padx=4, pady=4)

b1 = Button(janela, text='CLIQUE AQUI', background='beige', command=bemvindo)
b1.grid(column=40, row=15, padx=4, pady=4)



janela.mainloop()