# from tkinter import *
import tkinter as tk
class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.criarBotoes()

    def criarBotoes(self):
        # criar botões
        self.botao7 = tk.Button(self,text="7",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botao7.grid(row="1",column="1")
        self.botao8 = tk.Button(self,text="8",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botao8.grid(row="1",column="2")
        self.botao9 = tk.Button(self,text="9",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botao9.grid(row="1",column="3")
        self.botaodivisao = tk.Button(self,text="/",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botaodivisao.grid(row="1",column="4")
        self.botao4 = tk.Button(self,text="4",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botao4.grid(row="2",column="1")
        self.botao5 = tk.Button(self,text="5",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botao5.grid(row="2",column="2")
        self.botao6 = tk.Button(self,text="6",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botao6.grid(row="2",column="3")
        self.botaomultiplicacao = tk.Button(self,text="*",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botaomultiplicacao.grid(row="2",column="4")
        self.botao1 = tk.Button(self,text="1",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botao1.grid(row="3",column="1")
        self.botao2 = tk.Button(self,text="2",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botao2.grid(row="3",column="2")
        self.botao3 = tk.Button(self,text="3",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botao3.grid(row="3",column="3")
        self.botaosubtracao = tk.Button(self,text="-",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botaosubtracao.grid(row="3",column="4")
        self.botao0 = tk.Button(self,text="0",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botao0.grid(row="4",column="1")
        self.botaovirgula = tk.Button(self,text=",",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botaovirgula.grid(row="4",column="2")
        self.botaoigual = tk.Button(self,text="=",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botaoigual.grid(row="4",column="3")
        self.botaomais = tk.Button(self,text="+",fg="blue",background="gray",font=("Verdana","16","italic","bold"),height="1",width="4")
        self.botaomais.grid(row="4",column="4")
        

root = tk.Tk()        

# criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("Videoaulas Neri")
minhaAplicacao.master.maxsize(1920,1080)
minhaAplicacao.master.minsize(640,360)
# minhaAplicacao.master.geometry("800x600")

# inicia a aplicação
minhaAplicacao.mainloop()