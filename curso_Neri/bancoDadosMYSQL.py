import MySQLdb
con = MySQLdb.connect(db="cursopython",user="root",passwd="")
cur = con.cursor()


sql = "insert into pessoa values (?,?,?)"
dados=[(5,'Selvino Neitzke','selvino@gmail.com'),
       (6,'Romilda Neitzke','romilda@gmail.com'),
       (7,'lizete Neitzke','lizete@gmail.com'),
       (8,'joao Neitzke','joao@gmail.com')]
for registros in dados:
    cur.execute(sql,registros)

con.commit()

#ler os dados da tabela
sql = "select * from pessoa"
cur.execute(sql)

#recuperando o resultado da pesquisa
recset = cur.fetchall()

#listando dados do banco
for registros in recset:
    print(registros)
