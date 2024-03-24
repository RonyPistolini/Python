print("--------------------------------------------------------------------")
print("----------------- Sistema para cadastro de pessoas -----------------")
print("--------------------------------------------------------------------")

import oracledb
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

def cadastro(conexao):
    print("Digite os dados da pessoa:\n")
    nome = input("Nome: ")
    fone = input("Telefone: ")
    email = input("e-mail: ")
    cursor = conexao.cursor()
    sql="insert into pessoa (PESCODIGO,PESNOME,PESFONE,PESEMAIL) values (SEQ_PESSOA.NEXTVAL,'"+nome+"','"+fone+"','"+email+"')"
    try:
        cursor.execute(sql)
        conexao.commit()
        print("\nRegistro salvo com sucesso\n")
    except:
        print("Não foi possível gravar as informações no Banco de Dados")
        
    conexao.close()
    menu()

def listasTodos(conexao):
    cursor = conexao.cursor()
    sql="SELECT * FROM PESSOA ORDER BY PESCODIGO"
    try:
        cursor.execute(sql)
        dados_pessoas = cursor.fetchall()
        # quantidade = 0  
        print("----------------------------------------------------------")
        print("--------------------- Lista de Pessoas -------------------")
        print("----------------------------------------------------------")
        for dados in dados_pessoas:
            codigo=dados[0]
            nome=dados[2]
            fone=dados[1]
            email=dados[3]
            print("Código=%d, Nome=%s, Telefone=%s, e-mail=%s" % (codigo,nome,fone,email))
            # quantidade +=1
        # print("Quantidade de pessoas cadastradas: %d" % (quantidade))
        print("Quantidade de pessoas cadastradas: %d" % (len(dados_pessoas)))
        print("\n")
    except:
        print("Não foi possível listar as informações do Banco de Dados")
        
    conexao.close()
    menu()

def excluir(conexao):
    codigo=input("Digite o código da pessoa a ser excluída: ")    
    cursor = conexao.cursor()
    sql="DELETE FROM PESSOA WHERE PESCODIGO = '"+codigo+"'"
    try:
        cursor.execute(sql)
        conexao.commit()
        print("\nRegistro excluído com sucesso\n")
    except:
        print("Não foi possível excluir as informações no Banco de Dados")
        
    conexao.close()
    menu()

def pesquisar(conexao):
    nome=input("Digite o nome da pessoa a ser pesquisada: ")  
    cursor = conexao.cursor()
    sql="SELECT * FROM PESSOA WHERE PESNOME LIKE '%"+nome+"%'"
    try:
        cursor.execute(sql)
        dados_pessoas = cursor.fetchall()
        # quantidade = 0  
        print("----------------------------------------------------------")
        print("-------- Lista de Pessoas Encontradas na Pesquisa --------")
        print("----------------------------------------------------------")
        for dados in dados_pessoas:
            codigo=dados[0]
            nome=dados[2]
            fone=dados[1]
            email=dados[3]
            print("Código=%d, Nome=%s, Telefone=%s, e-mail=%s" % (codigo,nome,fone,email))
            # quantidade +=1
        # print("Quantidade de pessoas cadastradas: %d" % (quantidade))
        print("Quantidade de pessoas Encontradas: %d" % (len(dados_pessoas)))
        print("\n")
    except:
        print("Não foi possível pesquisar as informações no Banco de Dados")
        
    conexao.close()
    menu()

def alterar(conexao):
    codigo=input("Digite o código da pessoa a ser alterada: ")
    nome=input("Digite o novo nome da pessoa a ser alterada: ")
    cursor = conexao.cursor()
    sql="UPDATE PESSOA SET PESNOME='"+nome+"' WHERE PESCODIGO = '"+codigo+"'"
    try:
        cursor.execute(sql)
        conexao.commit()
        print("\nRegistro alterado com sucesso\n")
    except:
        print("Não foi possível alterar as informações no Banco de Dados")
        
    conexao.close()
    menu()

def menu():
    opcaoEscolhida = int(input("Escolha uma opção:\n\n1) Cadastrar\n2) Alterar\n3) Excluir\n4) Pesquisar\n5) Listar todos\n6) Sair\n\nOpção: "))
    try:
        if opcaoEscolhida < 1 or opcaoEscolhida > 6:
            print("Opção Inválida, escolha entre 1 e 6")
            menu()
    except:
        print("Opção Inválida, escolha entre 1 e 6")
        menu()

    conexao = conexaoBanco()
    if opcaoEscolhida == 1:
        cadastro(conexao)
    elif opcaoEscolhida == 5:
        listasTodos(conexao)
    elif opcaoEscolhida == 3:
        excluir(conexao)
    elif opcaoEscolhida == 4:
        pesquisar(conexao)
    elif opcaoEscolhida == 2:
        alterar(conexao)
    elif opcaoEscolhida == 6:
        SystemExit
        print("Sistema Finalizado")

menu()






