import sqlite3
#criar conexão com o banco de dados
con = sqlite3.connect("pessoas")
# com cursor podemos manipular o banco atraves de SQL
cur = con.cursor()

#inserir dados na tabela
#sql = "insert into pessoa values (4,'Gustavo Neitzke','gustavo@gmail.com')"
# cur.execute(sql)

# sql = "insert into pessoa values (?,?,?)"
# dados=[(5,'Selvino Neitzke','selvino@gmail.com'),
#        (6,'Romilda Neitzke','romilda@gmail.com'),
#        (7,'lizete Neitzke','lizete@gmail.com'),
#        (8,'joao Neitzke','joao@gmail.com')]
# for registros in dados:
#     cur.execute(sql,registros)

#cur.execute("delete from pessoa where pescodigo='2'")

con.commit()

#ler os dados da tabela
sql = "select * from pessoa"
cur.execute(sql)

#recuperando o resultado da pesquisa
recset = cur.fetchall()

#listando dados do banco
for registros in recset:
    print(registros)

