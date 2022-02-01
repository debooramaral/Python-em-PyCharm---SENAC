import tkinter as tk

app = tk.Tk()
app.geometry('600x600')
app.configure(background='white')
app.title("Primeira Tela")

menu = tk.Menu(app)

menuapp = tk.Menu(menu)
menuapp.add_command(label="Novo")
menuapp.add_command(label="Pesquisar")
menuapp.add_command(label="Deletar")
menuapp.add_separator()
menuapp.add_command(label='Sair')
menu.add_cascade(label="Cadastro", menu=menuapp)

app.config(menu=menu)

app.mainloop()