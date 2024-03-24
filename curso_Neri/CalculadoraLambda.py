from tkinter import *
import tkinter as tk
class App(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.criarComponentes()
    
    def criarComponentes(self):
        self.edit = tk.Entry(self.master,width=34)
        self.edit.grid(row=1,column=0)
        botoes = ["7","8","9","+","4","5","6","*","1","2","3","/","0","-","C","="]
        linha=1
        coluna=1
        for qualBotao in botoes:
            comando = lambda x=qualBotao:self.calcular(x)
            self.botao = tk.Button(self,text=qualBotao,width=6,height=2, command=comando)
            self.botao.grid(row=linha,column=coluna)
            if coluna >=4:
                linha +=1
                coluna =1
            else:
                coluna +=1
    def calcular(self,valor):
        if valor == "=":
            try:
                calculo = eval(self.edit.get())
                self.edit.insert(END,"="+str(calculo))
                valor = ""
            except:
                self.edit.insert(END,"ERRO")
        elif valor == "C":
            self.edit.delete(0,END)
            valor = ""
        self.edit.insert(END,valor)

root = tk.Tk()        

# criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("Videoaulas Neri")
minhaAplicacao.master.maxsize(1920,1080)
minhaAplicacao.master.minsize(352,198)
# minhaAplicacao.master.geometry("800x600")

# inicia a aplicação
minhaAplicacao.mainloop()