from tkinter import *
from os import popen
import os
import tkinter.messagebox
class Sistema:
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()
        self.menu = Menu(master)
        self.menuCadastro = Menu(self.menu)
        self.menuCadastro.add_command(label="Clientes",command=self.cadastraCliente)
        self.menuCadastro.add_command(label="Fornecedores")
        self.menuCadastro.add_command(label="Estoque")
        self.menu.add_cascade(label="Cadastro",menu=self.menuCadastro)
        self.menuConsulta = Menu(self.menu)
        self.menuConsulta.add_command(label="Clientes")
        self.menuConsulta.add_command(label="Fornecedores")
        self.menuConsulta.add_command(label="Estoque")
        self.menu.add_cascade(label="Consulta",menu=self.menuConsulta)
        self.menuFerramentas = Menu(self.menu)
        self.menuFerramentas.add_command(label="Calculadora",command=self.calculadora)
        self.menuFerramentas.add_command(label="Capturar Imagem",command=self.capturaImagem)
        self.menuFerramentas.add_command(label="Abrir Arquivo de Texto",command=self.chamaArquivoTexto)
        self.menu.add_cascade(label="Ferramentas",menu=self.menuFerramentas)
        self.menuFechar = Menu(self.menu)
        self.menuFechar.add_command(label="Sair",command=self.fechar)
        self.menu.add_cascade(label="Sair",menu=self.menuFechar)
        master.config(menu=self.menu)
    
    def cadastraCliente(self):
        print("clicou em cadastrar Cliente")

    def calculadora(self):
        popen("calc.exe")
        # os.startfile("calc.exe")

    def capturaImagem(self):
        popen("explorer.exe")
    
    def chamaArquivoTexto(self):
        os.startfile("texto.txt")
        # popen("texto.txt")
    
    def fechar(self):
        exit()

def sair():
    if tkinter.messagebox.askyesno("Fechar Janela","Tem certeza de que deseja fechar a janela?"):
        exit()
    else:
        pass

def menu():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW",sair)
    root.geometry("600x400")
    root.title("Sistema de Estoque")
    Sistema(root)
    root.mainloop()