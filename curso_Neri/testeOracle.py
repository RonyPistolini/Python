import oracledb

cnx = oracledb.connect(
    user = "hr",
    password="hr",
    dsn = "localhost/XEPDB1"
)
# cnx = oracledb.connect(
#     user = "system",
#     password="Melminie7037#",
#     dsn = "localhost/XEPDB1"
# )

cursor = cnx.cursor()

sql = "select * from COUNTRIES"


cursor.execute(sql)
records = cursor.fetchall()
for dados in records:
    print(dados)