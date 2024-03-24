# from tkinter import *
import tkinter as tk
class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.criarBotoes()

    def criarBotoes(self):
        botoes = ["7","8","9","+","4","5","6","*","1","2","3","/","0","-","C","="]
        linha=1
        coluna=1
        for qualBotao in botoes:
            self.botao = tk.Button(self,text=qualBotao,width=6,height=2)
            self.botao.grid(row=linha,column=coluna)
            if coluna >=4:
                linha +=1
                coluna =1
            else:
                coluna +=1

root = tk.Tk()        

# criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("Videoaulas Neri")
minhaAplicacao.master.maxsize(1920,1080)
minhaAplicacao.master.minsize(640,360)
# minhaAplicacao.master.geometry("800x600")

# inicia a aplicação
minhaAplicacao.mainloop()