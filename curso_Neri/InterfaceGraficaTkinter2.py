from tkinter import *
import tkinter.messagebox
class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.criarBotoes()
        self.criarLabels()
        self.entradaDados()

    def criarBotoes(self):
        # forma1 de criar botões
        self.botao = Button(self)
        self.botao["text"]="Bem vindo ao Python"
        self.botao["fg"]="red"
        self.botao["bg"]="yellow"
        self.botao["font"]=("Arial","16","italic","bold")
        self.botao["height"]=4
        self.botao["width"]=30
        self.botao["command"]=self.acaoImprimir
        self.botao.pack(side="top")

        # forma2 de criar botões
        self.botao1 = Button(self,text="Segundo Botão",fg="blue",background="gray",font=("Verdana","16","italic","bold"),command=self.acaoImprimir)
        self.botao1.pack(side="top")

        # botão sair
        self.botaoSaida = Button(self,text="Sair",fg="red",background="black",command=self.destroy)
        self.botaoSaida.pack(side="top")
    
    def criarLabels(self):
        self.label = Label(self)
        self.label["height"]=4
        self.label["width"]=30
        self.label["text"]="Bem vindo ao Python Label"
        self.label.pack(side="top")
    
    def entradaDados(self):
        self.edit = Entry(self)
        self.edit.pack(side="top")
    
    def acaoImprimir(self):
        print("Videoaulas Neri")
        print(self.edit.get())
        tkinter.messagebox.showinfo("titulo","informação")

# criando a aplicação
minhaAplicacao = App()

minhaAplicacao.master.title("Videoaulas Neri")
minhaAplicacao.master.maxsize(1920,1080)
minhaAplicacao.master.minsize(640,360)
# minhaAplicacao.master.geometry("800x600")

# inicia a aplicação
minhaAplicacao.mainloop()