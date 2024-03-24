import oracledb
from tkinter import *
Label(text="Cadastro de Pessoas",anchor=W,font=("Arial",20)).grid(row=1,column=1,columnspan=4,pady=5)
camposPessoa = ["Nome","Fone","Email"]
linha=2
for campos in camposPessoa:
    Label(text=campos,anchor=W,justify=LEFT).grid(row=linha,column=1,pady=5)
    Entry().grid(row=linha,column=2,pady=5)
    linha +=1
botaoGravar = Button(text="Gravar")
botaoGravar.grid(row=linha+1,column=1,pady=5)



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


mainloop()
