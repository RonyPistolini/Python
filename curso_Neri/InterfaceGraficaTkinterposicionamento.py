# from tkinter import *
import tkinter as tk
class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.criarBotoes()

    def criarBotoes(self):
        # criar botões
        self.botao1 = tk.Button(self,text="1 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao1.grid(row="1",column="1")
        self.botao2 = tk.Button(self,text="2 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao2.grid(row="1",column="2")
        self.botao3 = tk.Button(self,text="3 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao3.grid(row="2",column="1")
        self.botao4 = tk.Button(self,text="4 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao4.grid(row="2",column="2")
        self.botao5 = tk.Button(self,text="5 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao5.grid(row="3",column="1")
        self.botao6 = tk.Button(self,text="6 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao6.grid(row="3",column="3")
        self.botao1 = tk.Button(self,text="7 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao1.grid(row="4",column="1")
        self.botao2 = tk.Button(self,text="8 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao2.grid(row="1",column="5")
        self.botao3 = tk.Button(self,text="9 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao3.grid(row="2",column="6")
        self.botao4 = tk.Button(self,text="10 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao4.grid(row="3",column="6")
        self.botao5 = tk.Button(self,text="11 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao5.grid(row="1",column="6")
        self.botao6 = tk.Button(self,text="12 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao6.grid(row="3",column="4")

root = tk.Tk()        

# criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("Videoaulas Neri")
minhaAplicacao.master.maxsize(1920,1080)
minhaAplicacao.master.minsize(640,360)
# minhaAplicacao.master.geometry("800x600")

# inicia a aplicação
minhaAplicacao.mainloop()