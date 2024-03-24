# from tkinter import *
import tkinter as tk
class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.criarBotoes()

    def criarBotoes(self):
        # criar botões
        self.botao1 = tk.Button(self,text="1 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao1.pack(side="top")
        self.botao2 = tk.Button(self,text="2 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao2.pack(side="top")
        self.botao3 = tk.Button(self,text="3 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao3.pack(side="left")
        self.botao4 = tk.Button(self,text="4 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao4.pack(side="right")
        self.botao5 = tk.Button(self,text="5 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao5.pack(side="right")
        self.botao6 = tk.Button(self,text="6 Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"))
        self.botao6.pack(side="bottom")

root = tk.Tk()        

# criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("Videoaulas Neri")
minhaAplicacao.master.maxsize(1920,1080)
minhaAplicacao.master.minsize(640,360)
# minhaAplicacao.master.geometry("800x600")

# inicia a aplicação
minhaAplicacao.mainloop()