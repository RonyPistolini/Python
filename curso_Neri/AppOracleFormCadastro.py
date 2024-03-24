import oracledb
from tkinter import *

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

def excluir():
    botaoCancelar.configure(state="disabled")
    botaoAlterar.configure(state="disabled")
    botaoExcluir.configure(state="disabled")
    botaoGravar.configure(state="disabled")
    botaoNovo.configure(state="normal")
    conexao = conexaoBanco()
    codigo=editCodigo.get()
    cursor = conexao.cursor()
    sql="DELETE FROM PESSOA WHERE PESCODIGO = '"+codigo+"'"
    try:
        cursor.execute(sql)
        conexao.commit()
        limparCampos()
    except:
        print("Não foi possível excluir as informações no Banco de Dados")
    conexao.close()
    labelStatus['text']="Status: Registro Excluido com Sucesso"

def alterar():
    botaoCancelar.configure(state="disabled")
    botaoAlterar.configure(state="disabled")
    botaoExcluir.configure(state="disabled")
    botaoGravar.configure(state="disabled")
    botaoNovo.configure(state="normal")
    conexao = conexaoBanco()
    codigo=editCodigo.get()
    nome=editNome.get()
    fone=editFone.get()
    email=editEmail.get()
    cursor = conexao.cursor()
    sql="UPDATE PESSOA SET PESNOME='"+nome+"',PESFONE='"+fone+"',PESEMAIL='"+email+"' WHERE PESCODIGO = '"+codigo+"'"
    try:
        cursor.execute(sql)
        conexao.commit()
        print("\nRegistro alterado com sucesso\n")
    except:
        print("Não foi possível alterar as informações no Banco de Dados")
    conexao.close()
    limparCampos()
    labelStatus['text']="Status: Registro Alterado com Sucesso."

def cadastro():
    botaoCancelar.configure(state="disabled")
    botaoAlterar.configure(state="disabled")
    botaoExcluir.configure(state="disabled")
    botaoGravar.configure(state="disabled")
    botaoNovo.configure(state="normal")
    conexao = conexaoBanco()
    nome = editNome.get()
    fone = editFone.get()
    email = editEmail.get()
    cursor = conexao.cursor()
    sql="insert into pessoa (PESCODIGO,PESNOME,PESFONE,PESEMAIL) values (SEQ_PESSOA.NEXTVAL,'"+nome+"','"+fone+"','"+email+"')"
    try:
        cursor.execute(sql)
        conexao.commit()
        print("\nRegistro salvo com sucesso\n")
    except:
        print("Não foi possível gravar as informações no Banco de Dados")
        
    conexao.close()
    limparCampos()
    labelStatus['text']="Status: Novo Registro inserido com sucesso."

def novo():
    botaoCancelar.configure(state="normal")
    botaoAlterar.configure(state="disabled")
    botaoExcluir.configure(state="disabled")
    botaoGravar.configure(state="normal")
    botaoNovo.configure(state="disable")
    editCodigo.configure(state="normal")
    editCodigo.delete(0,END)
    editCodigo.configure(state="readonly")
    editNome.delete(0,END)
    editFone.delete(0,END)
    editEmail.delete(0,END)
    editNome.focus()
    labelStatus['text']="Status: Inserindo novo Registro"

def pesquisar():
    botaoCancelar.configure(state="normal")
    botaoAlterar.configure(state="normal")
    botaoExcluir.configure(state="normal")
    botaoGravar.configure(state="disabled")
    botaoNovo.configure(state="normal")
    conexao = conexaoBanco()
    cursor = conexao.cursor()
    sql="SELECT * FROM PESSOA WHERE UPPER(PESNOME) LIKE UPPER('%"+editPesquisa.get()+"%')"
    try:
        cursor.execute(sql)
        dados_pessoas = cursor.fetchone()
        limparCampos()
        editCodigo.configure(state="normal")
        editCodigo.insert(0,dados_pessoas[0])
        editCodigo.configure(state="readonly")
        # editCodigo.configure(state="disable")
        editNome.insert(0,dados_pessoas[2])
        editFone.insert(0,dados_pessoas[1])
        editEmail.insert(0,dados_pessoas[3])
    except:
        print("Não foi possível pesquisar as informações no Banco de Dados")
    conexao.close()
    labelStatus['text']="Pesquisa realizada com sucesso."

def limparCampos():    
    editCodigo.configure(state="normal")
    editCodigo.delete(0,END)    
    editCodigo.configure(state="readonly")
    editNome.delete(0,END)
    editFone.delete(0,END)
    editEmail.delete(0,END)
    editPesquisa.delete(0,END)
    editPesquisa.focus()

def cancelar():
    botaoCancelar.configure(state="disabled")
    botaoAlterar.configure(state="disabled")
    botaoExcluir.configure(state="disabled")
    botaoGravar.configure(state="disabled")
    botaoNovo.configure(state="normal")
    limparCampos()
    labelStatus['text']=""

#titulo
formPessoa = Tk()
formPessoa.title("Cadastro de Pessoas")
formPessoa.geometry("500x350+700+200")
titulo = Label(formPessoa,text="Cadastro de Pessoas")
titulo.grid(row=0,sticky=W+E+N+S,pady=10,padx=10)
separa = Frame(height=2, bd=1, relief=SUNKEN)
separa.grid(row=1,sticky=W+E+N+S,columnspan=4)

#pesquisa
labelPesquisa = Label(formPessoa,text="Pesquisar:")
labelPesquisa.grid(row=2,column=0,pady=15)
editPesquisa = Entry()
editPesquisa.grid(row=2,column=1,pady=15)
botaoPesquisa = Button(formPessoa,text="Pesquisar",command=pesquisar)
botaoPesquisa.grid(row=2,column=3,padx=10,pady=15)

#labels pessoa
labelCodigo = Label(formPessoa,text="Código:")
labelNome = Label(formPessoa,text="Nome:")
labelFone = Label(formPessoa,text="Telefone:")
labelEmail = Label(formPessoa,text="email:")

#entradas
editCodigo = Entry()
editNome = Entry()
editFone = Entry()
editEmail = Entry()

#posicionamento no formulario dos labels e edits de pessoa
labelCodigo.grid(row=4,sticky=W,padx=10)
editCodigo.grid(row=4,column=1,pady=5)
editCodigo.configure(state="readonly")
labelNome.grid(row=5,sticky=W,padx=10)
editNome.grid(row=5,column=1,pady=5)
labelFone.grid(row=6,sticky=W,padx=10)
editFone.grid(row=6,column=1,pady=5)
labelEmail.grid(row=7,sticky=W,padx=10)
editEmail.grid(row=7,column=1,pady=5)

#boto~es para manutenção de pessoas
botoes = Frame()
botaoNovo = Button(botoes,text="Novo",command=novo)
botaoGravar = Button(botoes,text="Gravar",command=cadastro)
botaoAlterar = Button(botoes,text="Alterar",command=alterar)
botaoExcluir = Button(botoes,text="Excluir",command=excluir)
botaoCancelar = Button(botoes,text="Cancelar",command=cancelar)

botaoNovo.grid(row=1,column=0,pady=10)
botaoGravar.grid(row=1,column=1,pady=10,padx=2)
botaoAlterar.grid(row=1,column=2,pady=10,padx=2)
botaoExcluir.grid(row=1,column=3,pady=10,padx=2)
botaoCancelar.grid(row=1,column=4,pady=10,padx=2)

labelStatus = Label(botoes,text="Status: ")
labelStatus.grid(row=2,column=1,columnspan=5,padx=2)

separa = Frame(height=2, bd=1, relief=SUNKEN)
separa.grid(row=8,sticky=W+E+N+S,columnspan=4,pady=10)
# configuração dos botoes
botoes.grid(row=9,column=1)

botaoCancelar.configure(state="disabled")
botaoAlterar.configure(state="disabled")
botaoExcluir.configure(state="disabled")
botaoGravar.configure(state="disabled")

mainloop()
