from tkinter import *
import tkinter.messagebox
class Login:
    def __init__(self,master):
        self.master = master
        self.master.title("Acesso ao Sistema")
        Label(self.master,text="Usuario e Senha").grid(row=1,column=1,columnspan=2,pady=10)
        Label(self.master,text="Usuario: ").grid(row=2,column=1,pady=5)
        self.usuario = Entry(self.master,width=30)
        self.usuario.grid(row=2,column=2)
        self.usuario.focus_force()
        Label(self.master,text="Senha: ").grid(row=3,column=1,pady=5)
        self.senha = Entry(self.master,width=30,show="*",fg="darkgray")
        self.senha.grid(row=3,column=2)
        self.status = Label(self.master,text="Status: ")
        self.status.grid(row=4,column=1,columnspan=2,pady=10)
        self.entrar = Button(self.master, width=7, text="OK", command=self.validarSenha)
        self.entrar.grid(row=5, column=1,pady=5,padx=5)
        self.loginSair = Button(self.master, width=7, text="Sair", command=self.fechar)
        self.loginSair.grid(row=5, column=2,pady=5,padx=5)

    def validarSenha(self):
        if self.usuario.get() == "neri" and self.senha.get() == "bonito":
            self.status['text'] = "Acesso Aprovado"
        else:
            self.status['text'] = "Acesso Reprovado"

    def fechar(self):
        self.master.destroy()

def sair():
    if tkinter.messagebox.askyesno("Fechar Janela","Tem certeza de que deseja fechar a janela?"):
        exit()
    else:
        pass


root=Tk()
root.geometry("370x250")
Login(root)
root.mainloop()
