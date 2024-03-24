import sqlite3
#criar conexão com o banco de dados
con = sqlite3.connect("pessoas")
# com cursor podemos manipular o banco atraves de SQL
cur = con.cursor()

# variavel para criar uma tabela no banco de dados
# sql = "create table pessoa"\
#     "(pescodigo integer primary key,"\
#     "pesnome varchar(40),"\
#     "pesemail varchar(50))"
# cur.execute(sql)

#inserir dados na tabela
sql = "insert into pessoa values (4,'Gustavo Neitzke','gustavo@gmail.com')"
cur.execute(sql)
con.commit()

#ler os dados da tabela
sql = "select * from pessoa"
cur.execute(sql)

#recuperando o resultado da pesquisa
recset = cur.fetchall()

#listando dados do banco
for registros in recset:
    print(registros)