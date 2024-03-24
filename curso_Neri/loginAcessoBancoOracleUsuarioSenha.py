from tkinter import *
import tkinter.messagebox
import oracledb
import menus
def conexaoBanco():
    try:
        con = oracledb.connect(
        user = "hr",
        password="hr",
        dsn = "localhost/XEPDB1"
        )
    except:
        print("Não foi possível conectar com o Banco de Dados")
        menu()

    return con
conexao = conexaoBanco()

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
        self.entrar = Button(self.master, width=7, text="OK", command=self.validarUsuarioSenha)
        self.entrar.grid(row=5, column=1,pady=5,padx=5)
        self.loginSair = Button(self.master, width=7, text="Sair", command=self.fechar)
        self.loginSair.grid(row=5, column=2,pady=5,padx=5)
        
    def validarUsuarioSenha(self):
        nomeLogin=""
        senhaLogin=""
        conexaoBanco()
        nome=self.usuario.get()
        senha=self.senha.get()
        cursor = conexao.cursor()
        sql="SELECT * FROM LOGIN WHERE USUARIO = '"+nome+"'"
        try:
            cursor.execute(sql)
            dados_login = cursor.fetchall()
            for dados in dados_login:
                nomeLogin=dados[0]
                senhaLogin=dados[1]
            if nome=='':
                nomeLogin="nomeInvalido"
                senhaLogin="senhaInvalida"
        except:
            self.status['text'] = "Não foi possível pesquisar as informações no Banco de Dados"
            
        
        if nome == nomeLogin and senha == senhaLogin:
            self.status['text'] = "Acesso Aprovado"
            menus.menu()
        else:
            self.status['text'] = "Acesso Reprovado"

    def fechar(self):
        conexao.close()
        self.master.destroy()

def sair():
    if tkinter.messagebox.askyesno("Fechar Janela","Tem certeza de que deseja fechar a janela?"):
        conexao.close()
        exit()
    else:
        pass


root=Tk()
root.protocol("WM_DELETE_WINDOW",sair)
root.geometry("370x250")
Login(root)
root.mainloop()
