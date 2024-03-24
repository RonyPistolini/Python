from tkinter import *
import tkinter.messagebox
class Conteiners:
    def __init__(self,master):
        self.conteiner1 = Frame(master)
        self.conteiner2 = Frame(master)
        self.conteiner3 = Frame(master)
        self.conteinerSeparador = Frame(height=20,width=250,bd=2,relief=SUNKEN)
        self.conteiner1.pack()
        self.conteinerSeparador.pack()
        self.conteiner2.pack()
        self.conteiner3.pack()
        self.botao1 = Button(self.conteiner1,text="Botão 1").pack()
        self.botao2 = Button(self.conteiner2,text="Botão 2").pack(side="right")
        self.botao3 = Button(self.conteiner2,text="Botão 3").pack(side="left")
        self.botao4 = Button(self.conteiner3,text="Botão 4 - Sair",command=self.fechar).pack()

    def fechar(self):
        exit()

def sair():
    if tkinter.messagebox.askyesno("Fechar Janela","Tem certeza de que deseja fechar a janela?"):
        exit()
    else:
        pass

root = Tk()
root.protocol("WM_DELETE_WINDOW",sair)
Conteiners(root)
root,mainloop()
