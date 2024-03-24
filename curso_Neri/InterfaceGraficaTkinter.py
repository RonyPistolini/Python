from tkinter import *
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
        self.botao.pack(side="top")

        # forma2 de criar botões
        self.botao1 = Button(self,text="Segundo Botão",fg="blue",background="gray")
        self.botao1.pack(side="top")
    
    def criarLabels(self):
        self.label = Label(self)
        self.label["text"]="Bem vindo ao Python Label"
        self.label.pack(side="top")
    
    def entradaDados(self):
        self.edit = Entry(self)
        self.edit.pack(side="top")

# criando a aplicação
minhaAplicacao = App()

minhaAplicacao.master.title("Videoaulas Neri")
minhaAplicacao.master.maxsize(1920,1080)
minhaAplicacao.master.minsize(640,360)
# minhaAplicacao.master.geometry("800x600")

# inicia a aplicação
minhaAplicacao.mainloop()