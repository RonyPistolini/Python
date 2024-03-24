import oracledb
import sys
from tkinter import *
listaPessoas =Tk()
listaPessoas.title("Lista de Pessoas Cadastradas")
def conexaoBanco():
    try:
        con = oracledb.connect(
        user = "hr",
        password="hr",
        dsn = "localhost/XEPDB1"
        )
    except:
        print("Não foi possível conectar com o Banco de Dados")

    return con

conexao = conexaoBanco()
cursor = conexao.cursor()
sql="SELECT * FROM PESSOA ORDER BY PESCODIGO"
try:
    cursor.execute(sql)
    dados_pessoas = cursor.fetchall()
    linha=0
    coluna=1
    corlinha="white"
    Label(text="Lista de Pessoas",font=("Arial","12"),relief=RIDGE,width=66,anchor=CENTER,bg="gray",fg="white").grid(row=linha,column=coluna,columnspan=4,pady=5)
    Label(text="Código",relief=RIDGE,width=7,anchor=CENTER,bg="darkgray").grid(row=linha+1,column=coluna)
    Label(text="Nome",relief=RIDGE,width=30,anchor=CENTER,bg="darkgray").grid(row=linha+1,column=coluna+1)
    Label(text="Telefone",relief=RIDGE,width=15,anchor=CENTER,bg="darkgray").grid(row=linha+1,column=coluna+2)
    Label(text="e-mail",relief=RIDGE,width=30,anchor=CENTER,bg="darkgray").grid(row=linha+1,column=coluna+3)
    for dados in dados_pessoas:
        codigo=dados[0]
        nome=dados[2]
        fone=dados[1]
        email=dados[3]
        if linha % 2 == 0:
            corlinha="lightgray"
        else:
            corlinha="white"
        Label(text=codigo,relief=RIDGE,width=7,anchor=CENTER,bg=corlinha).grid(row=linha+2,column=coluna)
        Label(text=nome,relief=RIDGE,width=30,anchor=W,bg=corlinha).grid(row=linha+2,column=coluna+1)
        Label(text=fone,relief=RIDGE,width=15,anchor=CENTER,bg=corlinha).grid(row=linha+2,column=coluna+2)
        Label(text=email,relief=RIDGE,width=30,anchor=W,bg=corlinha).grid(row=linha+2,column=coluna+3)
        linha +=1
    quantidade = ("Quantidade de Pessoas Cadastradas: %d" % len(dados_pessoas))
    Label(text=quantidade,relief=RIDGE,width=85,anchor=W,bg="gray",fg="white").grid(row=linha+3,column=coluna,columnspan=4)
except:
    print("Não foi possível listar as informações do Banco de Dados")
        
conexao.close()
mainloop()
